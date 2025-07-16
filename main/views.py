from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import Text, Test, ProgrammingLanguage
from django.db.models import Q
import json
from .tasks import sql_checker, replace_html_tags

tests = []

def typer(request: HttpRequest):
    test_id = 0 or request.GET.get("test_id")
    return render(request, 'main/typer.html', {"test_id": test_id, "langs": ProgrammingLanguage.objects.all()})


def text(request: HttpRequest):
    text = None
    lang = None
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        test_id = data.get("test_id")
        lang = data.get("lang")

        if test_id and test_id != 'None':
            test = Test.objects.get(id=test_id)
            if test:
                text = test.text
                prolang = test.text.prolang

    if not text:
        if lang is None or lang == "random" or lang == "Random":
            text = Text.objects.order_by('?')[0]
            prolang = text.prolang
        else:
            prolang = ProgrammingLanguage.objects.get(Q(short_name=lang) | Q(name=lang))
            text = Text.objects.filter(prolang=prolang).order_by('?')[0]
    if request.user.is_authenticated:
        test = Test.objects.create(text=text, user=request.user)
    else:
        test = Test.objects.create(text=text)

    response = JsonResponse({
        "text": text.text.split("\n"),
        "id": text.id,
        "pl_name": prolang.name,
        "prolang": prolang.short_name,
        "tab_count": prolang.tab_count,
        "test_id": test.id
    })
    return response


def result(request: HttpRequest):
    context = {}
    if request.method == "POST":
        try:
            body = json.loads(request.body.decode("utf-8"))
            test = Test.objects.get(id=body.get("test_id"))

            text_lines = test.text.text.split("\r\n")
            lines = body.get("inputs")

            correct = 0
            incorrect = 0
            total = -1
            full_text = ""

            for i in range(len(text_lines)):
                text_line = text_lines[i]
                total += len(text_line) + 1

                if len(lines) <= i:
                    full_text += replace_html_tags(line) + "\n"
                    continue
                line = lines[i]
                for c in range(len(line)):
                    if len(text_line) <= c:
                        full_text += "<span-class='incorrect'>" + \
                            replace_html_tags(line[c:]) + "</span>\n"
                        break

                    symbol = replace_html_tags(line[c])
                    if line[c] == text_line[c]:
                        full_text += "<span-class='correct'>" + symbol + "</span>"
                        correct += 1
                    else:
                        if test.text.prolang.short_name == "sql":
                            if sql_checker(text_line, c, symbol):
                                full_text += "<span-class='correct'>" + symbol + "</span>"
                                correct += 1
                                continue
                        full_text += "<span-class='incorrect'>" + symbol + "</span>"
                        incorrect += 1
                
                if len(line) < len(text_line):
                    full_text += replace_html_tags(text_line[len(line):])

                full_text += "\n"
                correct += 1

            accuracy = (correct - 1) / total
            time = body.get("end_time") - body.get("start_time")
            wpm = (correct + incorrect) / 5 / (time / 60000)

            lang = test.text.prolang

            context = {
                "prolang": lang.name,
                "source": test.text.source,
                "source_url": test.text.source_link or "#",
                "wpm": round(wpm, 1),
                "accuracy": round(accuracy * 100, 2),
                "duration": round(time / 1000.0, 1),
                "full_text": full_text.replace("\n", "<br>").replace(" ",
                            "&nbsp;").replace("span-class", "span class"),
                "test_id": test.id
            }

            test.complete = True
            test.time = int(time)
            test.wpm = wpm
            test.accuracy = accuracy
            test.save()
        except Exception as e:
            print(e)

    return render(request, 'main/result.html', context)


def hints(request: HttpRequest):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        from .hints import get_hints
        hints = get_hints(data)
        return JsonResponse({"hints": hints})
