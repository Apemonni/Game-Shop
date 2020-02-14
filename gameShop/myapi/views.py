from django.shortcuts import render

from rest_framework import viewsets

from .serializers import GameDataSerializer, GameSerializer, ProfileSerializer, UserSerializer
from play_game.models import GameData
from shop.models import Game
from users.models import Profile
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework import permissions
from .permissions import IsAdminUserOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class GameDataViewSet(viewsets.ModelViewSet):
    queryset = GameData.objects.all()
    serializer_class = GameDataSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    try:
        user = self.request.user
        userobject = Profile.objects.get(user = user)
        if userobject.is_dev:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUserOrReadOnly]
    except:
        permission_classes = [IsAdminUserOrReadOnly]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]
