from django.db import models

class AllHighScores(models.Model):
    user_id = models.CharField(max_length=200)
    user_score = models.PositiveIntegerField()
    game_id = models.CharField(max_length=200)
    score_date = models.DateTimeField()
