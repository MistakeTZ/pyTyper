from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import Text
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .pytext import get_attributes, custom_key, get_context

def typer(request: HttpRequest):
    return render(request, 'main/typer.html')


@csrf_exempt
def text(request: HttpRequest):
    text = Text.objects.order_by('?')[0]
    return JsonResponse({
        "text": text.text.split("\n"),
        "id": text.id,
        "programming_language": text.programming_language
    })


@csrf_exempt
def hints(request: HttpRequest):
    hints = []
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            words = [word for word in data.get("inputs") if word]
            line = words[-1].split()
            word = data.get("word")
            if "(" in word:
                word = word.split("(")[-1]
            context = get_context(words[:-1])

            before_point = word.split(".")[0] if "." in word else None
            
            for key in context:
                if key.startswith(word):
                    hints.append(key)

            with open(settings.BASE_DIR / "static/main/hints/basic.txt", "r") as f:
                hints.extend(f.readlines())
            if len(line) >= 2:
                if line[0] == "import" or (len(line) == 2 and line[0] == "from"):
                    with open(settings.BASE_DIR / "static/main/hints/modules.txt", "r") as f:
                        hints.extend(f.readlines())
                        if not before_point:
                            hints = [h for h in hints if not "." in h]

            if before_point in context:
                cont = context[before_point]
                after_point = word[word.index(".") + 1:]
                hints.extend([before_point + "." + hint for
                    hint in get_attributes(cont) if hint.startswith(after_point)])
            
            hints = [hint.strip("\n") for hint in hints if hint.startswith(word)]
        except Exception as e:
            print(e)

    return JsonResponse({"hints": sorted(list(set(hints)), key=custom_key), "context": context})
