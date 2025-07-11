from django.shortcuts import render
from django.http import HttpRequest

def typer(request: HttpRequest):
    return render(request, 'main/typer.html')
