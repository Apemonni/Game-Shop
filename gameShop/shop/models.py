from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    price = models.PositiveIntegerField()
    source = models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games')

    def __str__(self):
        return self.name

    # Needed for redirect after adding new game
    def get_absolute_url(self):
        return reverse('game-detail', kwargs={'pk': self.pk})


    # TODO: Make fields visible on admin page


# This might not be needed after all

# TESTING WITH THIS TABLE
class AllHighScores(models.Model):
    user_id = models.CharField(max_length=200)
    user_score = models.PositiveIntegerField()
    game_id = models.CharField(max_length=200)
    score_date = models.DateTimeField()
