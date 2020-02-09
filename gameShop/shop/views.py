# Django
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
# Use for restricting access on class-based views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Use for restricting access on method-based views
#from django.contrib.auth.decorators import login_required

# Models
from .models import Game, AllHighScores
from users.models import Profile
from play_game.models import GamePurchase

def home(request):
    return render(request, 'shop/index.html')

class GameListView(ListView):
    model = Game
    #template_name = '' # use if different than game_list.html
    #context_object_name = 'games' # name used in the template, default is 'object'
    #ordering = ['name'] # attribute(s) to order by, prepend with '-'sign to reverse


class GameDetailView(DetailView):
    model = Game

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        game = self.get_object()
        user = self.request.user
        is_purchased = GamePurchase.objects.filter(user=user, game=game).first() != None
        times_purchased = len(GamePurchase.objects.filter(game=game))
        context['game_purchased'] = is_purchased
        context['times_purchased'] = times_purchased

        return context
        


class GameCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Game
    fields = ['name', 'description', 'price', 'source']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.profile.is_dev == True


class GameUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Game
    fields = ['name', 'description', 'price', 'source']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        is_dev = self.request.user.profile.is_dev
        is_owner = self.get_object().author == self.request.user
        return is_dev and is_owner


class GameDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Game
    success_url = '/home'

    def test_func(self):
        is_dev = self.request.user.profile.is_dev
        is_owner = self.get_object().author == self.request.user
        return is_dev and is_owner


def buy_confirm(request, game_id):
    game = Game.objects.get(pk=game_id)
    return render(request, 'shop/buy_game.html', {'game': game})



def buy(request, game_id):
    user = request.user
    game = Game.objects.get(pk=game_id)
    GamePurchase.objects.create(game=game, user=user, purchase_price=game.price)
    return render(request, 'shop/buy_success.html')

def highscores(request):
    #score = get_object_or_404(AllHighScores)
    score = AllHighScores.objects.all() # USING AllHighScores JUST FOR TESTING
    return render(request, 'shop/highscores_details.html', {'score': score})
