from django.urls import path

from . import views

urlpatterns = [
    path('', views.highscores, name='highscores'),
]
