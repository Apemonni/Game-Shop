from django.urls import path
from django.views.generic import TemplateView

from . import views

#app_name = 'PlayGame'

urlpatterns = [
    path('<int:game_id>/', views.play, name='play-game'),
    path('load/<int:game_id>/', views.load, name='load'),
    path('save/<int:game_id>/', views.save, name='save'),
    path('test_game2/', TemplateView.as_view(template_name='test_game3.html')),
    path('score/<int:game_id>/', views.submit_score, name='submit-score'),
]
