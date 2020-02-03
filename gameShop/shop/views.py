from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import AllHighScores

def highscores(request):
    score = get_object_or_404(AllHighScores)
