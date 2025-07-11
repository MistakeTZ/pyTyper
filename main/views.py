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
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            words = [word for word in data.get("inputs") if word]
            line = words[-1].split()
            word = data.get("word")
            
            hints = ["import"]
            if len(line) >= 2:
                if line[-2] == "import":
                    with open(settings.BASE_DIR / "static/main/hints/modules.txt", "r") as f:
                        hints.extend(f.readlines())
        except:
            pass
    return JsonResponse({"hints": hints})
