from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from shop.models import Game

class GamePurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(default=timezone.now)
    purchase_price = models.PositiveSmallIntegerField()

class GameData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    highscore = models.PositiveIntegerField()
    save_data = models.TextField()
