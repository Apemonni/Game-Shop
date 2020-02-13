from rest_framework import serializers
from play_game.models import GameData
from shop.models import Game
from users.models import Profile
from django.contrib.auth.models import User

class GameDataSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = GameData
        fields = ('game','id','highscore','save_data')

class GameSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Game
        fields = ('name', 'description', 'source', 'times_played')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ('user', 'is_dev')

'''class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')'''
