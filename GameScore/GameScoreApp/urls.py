from django.urls import path

from . import views

urlpatterns = [
    path("", views.mainPage, name="index"),
    path("gamepage", views.gamePage, name="gamePage"),
    path("gamereviewpage", views.gameReviewView, name="gameReviewView"),
    path("submitreview", views.submitReview, name="submitReview"),
    path("login", views.login, name="login"),
    path("signUp", views.signUp, name="signUp"),
]
