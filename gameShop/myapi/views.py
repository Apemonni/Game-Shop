from django.shortcuts import render

from rest_framework import viewsets

from .serializers import GameDataSerializer, GameSerializer, ProfileSerializer
from play_game.models import GameData
from shop.models import Game
from users.models import Profile
from rest_framework import generics
from django.contrib.auth.models import User

'''class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer'''

class GameDataViewSet(viewsets.ModelViewSet):
    queryset = GameData.objects.all()
    serializer_class = GameDataSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
