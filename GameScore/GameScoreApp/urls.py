from django.urls import path

from . import views

urlpatterns = [
    path("", views.mainPage, name="index"),
    path("gamepage", views.gamePage, name="gamePage"),
    path("gameReviewView", views.gameReviewView, name="gameReviewView"),
]
