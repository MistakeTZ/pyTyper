from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from .models import Text
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .pytext import get_attributes, custom_key, get_context
import jedi

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
    if request.method == "POST":
        try:
            import datetime, math, subprocess
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

