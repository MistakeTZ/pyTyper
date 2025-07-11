from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import Text
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

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
    context = {"i": "int", "f": "float", "s": "str", "b": "bool", "l": "list", "d": "dict"}
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            words = [word for word in data.get("inputs") if word]
            line = words[-1].split()
            word = data.get("word")
            # context = data.get("context")

            before_point = word.split(".")[0] if "." in word else None
            
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
                if cont == "int":
                    hints.extend([before_point + "." + hint for hint in dir(int) if hint.startswith(after_point)])
                elif cont == "str":
                    hints.extend([before_point + "." + hint for hint in dir(str) if hint.startswith(after_point)])
                elif cont == "bool":
                    hints.extend([before_point + "." + hint for hint in dir(bool) if hint.startswith(after_point)])
                elif cont == "float":
                    hints.extend([before_point + "." + hint for hint in dir(float) if hint.startswith(after_point)])
                elif cont == "list":
                    hints.extend([before_point + "." + hint for hint in dir(list) if hint.startswith(after_point)])
                elif cont == "dict":
                    hints.extend([before_point + "." + hint for hint in dir(dict) if hint.startswith(after_point)])
            
            hints = [hint.strip("\n") for hint in hints if hint.startswith(word)]
        except Exception as e:
            print(e)

    return JsonResponse({"hints": sorted(list(set(hints)), key=custom_key), "context": context})


def custom_key(s):
    # Заменяем символ _ на символ с очень высоким Unicode-кодом для сортировки
    return s.replace('_', chr(0x10FFFF))