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


@csrf_exempt
def result(request: HttpRequest):
    if request.method == "POST":
        print(request.body.decode("utf-8"))
    return render(request, 'main/result.html')
