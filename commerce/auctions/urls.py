from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("login/", views.login_, name="login"),
    path("logout/", views.logout_, name="logout"),
    path("register/", views.register, name="register"),
    path("listings/", views.index, name="index"),
    path("listings/<str:title>/", views.listing, name="listing"),
    path("listings/<str:title>/watchlist/", views.watchlist, name="watchlist"),
    path("watchlist/", views.displayWatchlist, name="displayWatchlist"),
    path("categories/", views.categories, name="categories"),
    path("categories/<str:category>/", views.categoriesFiltered, name="categoriesFiltered"),
    path("create/", views.create, name="create"),
]
