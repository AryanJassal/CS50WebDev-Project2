from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

class User(AbstractUser):
    pass

class Listing(models.Model):
    owner = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    indexDescription = models.CharField(max_length=255)
    imageURL = models.URLField()
    price = models.IntegerField()
    numberBids = models.IntegerField()
    category = models.CharField(max_length=64)
    whenMade = models.DateTimeField(default=datetime.now, editable=False)

    def __str__(self):
        return f"By {self.owner}: {self.title}; Current Bid: ${self.price}; Category: {self.category}"

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

    def __str__(self):
        return f"Product: {self.product}"

class CurrentBid(models.Model):
    user = models.CharField(max_length=64)
    listing = models.CharField(max_length=64)

class Categories(models.Model):
    category = models.CharField(max_length=32)

    def __str__(self):
        return self.category