from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User
from .models import *

def index(request):
    return render(request, "auctions/index.html")

def login_(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auction/login.html", {
                "message": "Invalid username and/or password."
            })
    elif request.method == "GET":
        return render(request, "auctions/login.html")

def logout_(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmPassword = request.POST["confirmPassword"]

        if password != confirmPassword:
            return render(request, "auctions/register.html", {
                "message": "The passwords do not match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })

        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    elif request.method == "GET":
        return render(request, "auctions/register.html")

@login_required
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        desctiption = request.POST["description"]
        startingBid = request.POST["startingBid"]
        imageURL= request.POST["imageURL"]
        category = request.POST["category"]

        listing = Listing(
            user = "a",
            title = title,
            description = description,
            startingBid = startingBid,
            imageURL = imageURL,
            category = category
        )