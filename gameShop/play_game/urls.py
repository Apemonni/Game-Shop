from django.urls import path

from . import views

#app_name = 'PlayGame'

urlpatterns = [
    path('<int:game_id>/', views.play, name='play-game'),
    path('load/<int:game_id>/', views.load, name='load'),
    path('save/<int:game_id>/', views.save, name='save'),
    path('score/<int:game_id>/', views.submit_score, name='submit-score'),
]
