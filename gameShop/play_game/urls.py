from django.urls import path

from . import views

#app_name = 'PlayGame'

urlpatterns = [
path('', views.play, name='index'),
path('<load/', views.load, name='load'),
path('<save/', views.save, name='save'),
]
