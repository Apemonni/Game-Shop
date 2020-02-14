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
from .permissions import IsAdminUserOrReadOnly, AdminReadOnly, ReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AdminReadOnly] #only admins can read user data

class GameDataViewSet(viewsets.ModelViewSet):
    queryset = GameData.objects.all()
    serializer_class = GameDataSerializer
    permission_classes = [ReadOnly] #read only permission for all

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    try:
        user = self.request.user
        userobject = Profile.objects.get(user = user)
        #cheking wheter user is developper (or admin), if it is true user can add games to database through API
        if userobject.is_dev:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUserOrReadOnly]
    except:
        permission_classes = [IsAdminUserOrReadOnly] #read only acces only for players and anonymous users


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer #only admins can see profile data
    permission_classes = [AdminReadOnly]
