from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Game, AllHighScores
#from play_game import GamePurchase

def home(request):
    return render(request, 'shop/index.html')

class GameListView(ListView):
    model = Game
    #template_name = '' # use if different than game_list.html
    #context_object_name = 'games' # name used in the template, default is 'object'
    #ordering = ['name'] # attribute(s) to order by, prepend with '-'sign to reverse


class GameDetailView(DetailView):
    model = Game


class GameCreateView(CreateView):
    model = Game
    fields = ['name', 'description', 'price', 'source']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class GameUpdateView(UpdateView):
    model = Game
    fields = ['name', 'description', 'price', 'source']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class GameDeleteView(DeleteView):
    model = Game
    success_url = '/home'

def highscores(request):
    #score = get_object_or_404(AllHighScores)
    score = AllHighScores.objects.all() # USING AllHighScores JUST FOR TESTING
    return render(request, 'shop/highscores_details.html', {'score': score})
