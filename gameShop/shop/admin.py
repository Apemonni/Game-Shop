from django.contrib import admin
from .models import Game, AllHighScores

# Register your models here.
admin.register(Game, AllHighScores)