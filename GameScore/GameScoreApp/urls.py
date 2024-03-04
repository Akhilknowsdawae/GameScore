from django.urls import path

from . import views

urlpatterns = [
    path("", views.mainPage, name="index"),
    path("login/", views.sign_in, name='login'),
    path("signup/", views.sign_up, name='signup'),
]
