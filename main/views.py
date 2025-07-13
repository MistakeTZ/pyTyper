from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import Text, Test
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import jedi


tests = []

def typer(request: HttpRequest):
    return render(request, 'main/typer.html')


@csrf_exempt
def text(request: HttpRequest):
    text = Text.objects.order_by('?')[0]
    test = Test.objects.create(text=text, user=request.user)

    return JsonResponse({
        "text": text.text.split("\n"),
        "id": text.id,
        "programming_language": text.programming_language,
        "test_id": test.id
    })


@csrf_exempt
def hints(request: HttpRequest):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            lines = [line for line in data.get("inputs") if line]

            if not lines:
                return JsonResponse({'hints': []})

            current_line = lines[-1]
            full_code = '\n'.join(lines)
            line_number = len(lines)
            column = len(current_line)
            script = jedi.Script(code=full_code)

            completions = script.complete(line=line_number, column=column)
            suggestions = [c.name for c in completions]

            return JsonResponse({'hints': suggestions})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({"error": "Request method is not POST"}, status=400)


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

            for i in range(len(text_lines)):
                text_line = text_lines[i]
                total += len(text_lines) + 1

                if len(lines) <= i:
                    continue
                line = lines[i]
                for c in range(len(line)):
                    if len(text_line) <= c:
                        break

                    if line[c] == text_line[c]:
                        correct += 1
                        if len(line) == c + 1 and len(lines) != i + 1:
                            correct += 1
                    else:
                        incorrect += 1

            accuracy = correct / total
            time = body.get("end_time") - body.get("start_time")
            wpm = (correct + incorrect) / 5 / (time / 60000)

            context = {
                "programming_language": test.text.programming_language,
                "source_url": test.text.source,
                "wpm": round(wpm, 1),
                "accuracy": round(accuracy * 100, 2),
                "duration": round(time / 1000.0, 1),
                "full_text": test.text.text
            }

            test.complete = True
            test.time = int(time)
            test.wpm = wpm
            test.accuracy = accuracy
            test.save()
        except Exception as e:
            print(e)

    return render(request, 'main/result.html', context)
