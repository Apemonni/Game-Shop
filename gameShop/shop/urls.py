from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('highscores/', views.highscores, name='highscores'),
    path('home/', views.home, name='shop-home'),
    path('', RedirectView.as_view(pattern_name='shop-home')),
]
