from django.contrib.auth.models import AbstractUser
from django.db import models


class UserReview(AbstractUser):
    description = models.TextField(max_length=1000)


class Game(models.Model):
    name = models.CharField(max_length=100)
    releaseDate = models.DateField()
    description = models.TextField(max_length=1000)
    overallRating = models.IntegerField()


class Review(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    score = models.IntegerField()

    userID = models.ForeignKey(UserReview, on_delete=models.CASCADE)
    gameID = models.ForeignKey(Game, on_delete=models.CASCADE)
