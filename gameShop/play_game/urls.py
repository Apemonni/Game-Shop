from django.urls import path

from . import views

#app_name = 'PlayGame'

urlpatterns = [
path('<int:game_id>/', views.play, name='play-game'),
path('<load/', views.load, name='load'),
path('<save/', views.save, name='save'),
]
