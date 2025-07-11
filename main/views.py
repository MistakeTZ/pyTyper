from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import Text
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
