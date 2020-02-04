from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import AllHighScores

def home(request):
    return render(request, 'shop/index.html')

def highscores(request):
    #score = get_object_or_404(AllHighScores)
    return render(request, 'shop/highscores_details.html')
