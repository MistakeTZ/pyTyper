from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.typer, name='typer'),
    path('text', views.text, name='text'),
    path('api/hints', views.hints, name='hints'),
]