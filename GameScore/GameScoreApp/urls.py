from django.urls import path

from . import views

urlpatterns = [
    path("", views.mainPage, name="index"),
    path("signup/", views.sign_up, name="signup"),
]