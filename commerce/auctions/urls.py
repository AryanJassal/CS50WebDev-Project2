from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_, name="login"),
    path("logout/", views.logout_, name="logout"),
    path("register/", views.register, name="register"),
    path("listings/", views.index, name="listings"),
    path("listings/create/", views.create, name="create"),
]
