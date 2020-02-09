from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('highscores/', views.highscores, name='highscores'),
    path('home/', views.home, name='shop-home'),
    path('games/', views.GameListView.as_view(), name='game-list'),
    path('games/<int:pk>/', views.GameDetailView.as_view(), name='game-detail'),
    path('games/new/', views.GameCreateView.as_view(), name='game-create'),
    path('games/<int:pk>/edit/', views.GameUpdateView.as_view(), name='game-update'),
    path('games/<int:pk>/delete/', views.GameDeleteView.as_view(), name='game-delete'),
    path('games/<int:game_id>/buy/', views.buy_confirm, name='buy-confirm'),
    path('games/<int:game_id>/buy/success/', views.buy, name='buy-game'),
    path('', RedirectView.as_view(pattern_name='shop-home')),
]
