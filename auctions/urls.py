from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),
    path('register/', views.register, name='register'),
    path('listings/', views.index, name='index'),
    path('listings/<int:pk>/', views.listing, name='listing'),
    path('listings/<int:pk>/watchlist/', views.watchlist, name='watchlist'),
    path('watchlist/', views.displayWatchlist, name='displayWatchlist'),
    path('categories/', views.categories, name='categories'),
    path('categories/<str:slug>/', views.categoriesFiltered, name='categoriesFiltered'),
    path('create/', views.create, name='create'),
    path('<int:pk>/bid/', views.bid, name='bid'),
    path('<int:pk>/close/', views.closeBid, name='closeBid'),
    path('<int:pk>/comment/', views.comment, name='comment')
]
