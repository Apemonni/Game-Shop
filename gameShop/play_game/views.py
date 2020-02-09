from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, redirect

from shop.models import Game
from .models import GameData, GamePurchase


def load(request, player_id, game_id):
    #Should decide where gamestate models are held that these views process?
    return HttpResponse("Loading the game")

def save(request, game_id):
    game = Game.objects.get(pk=game_id)
    a = GameData(user_id = request.user, game_id = game, highscore = 0, save_data = str(request.GET))
    a.save()
    return HttpResponseRedirect(reverse('play-game', args=(game.id,)))

    #Should decide where gamestate models are held that these views process?


def play(request, game_id):
    game = Game.objects.get(pk=game_id)
    user = request.user
    return render(request, 'play_game/play.html', {'game': game}, {'user': user})
