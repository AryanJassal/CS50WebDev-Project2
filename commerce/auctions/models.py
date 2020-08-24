from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Listing(models.Model):
    user = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    imageURL = models.TextField(blank=True)
    price = models.IntegerField()
    numberBids = models.IntegerField()
    category = models.CharField(max_length=64)

class Bid(models.Model):
    product = models.CharField(max_length=64)
    user = models.CharField(max_length=64)
    price = models.IntegerField()

class Comment(models.Model):
    user = models.CharField(max_length=64)
    comment = models.CharField(max_length=255)

class Watchlist(models.Model):
    user = models.CharField(max_length=64)
    product = models.CharField(max_length=64)

class CurrentBid(models.Model):
    user = models.CharField(max_length=64)
    listing = models.CharField(max_length=64)