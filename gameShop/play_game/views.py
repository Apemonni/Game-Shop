from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from shop.models import Game, GamePurchase
from .models import GameData


def load(request, player_id, game_id):
    #Should decide where gamestate models are held that these views process?
    return HttpResponse("Loading the game")

def save(request, game_id):
    game = Game.objects.get(pk=game_id)
    a = GameData(user = request.user, game = game, highscore = 0, save_data = str(request.GET))
    a.save()
    return HttpResponseRedirect(reverse('play-game', args=(game.id,)))

    #Should decide where gamestate models are held that these views process?

@login_required
def play(request, game_id):
    game = Game.objects.get(pk=game_id)

    # Only allow the game's author and users who have bought the game to play
    if request.user != game.author and request.user.purchases.filter(game=game).count() == 0:
        return HttpResponseForbidden('You have not purchased this game yet.')

    game.times_played += 1
    game.save()
    return render(request, 'play_game/play.html', {'game': game})
