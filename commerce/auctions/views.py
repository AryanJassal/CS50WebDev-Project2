from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Bid, Comment, Watchlist, CurrentBid

wishlisted = None

categories = ["Technology", "Food", "Transportation", "Home",
              "Utilities", "Hobby", "Sports", "Fashion", "Other"]


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


def login_(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
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
def create(request, user):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        startingBid = request.POST["startingBid"]
        imageURL = request.POST["imageURL"]
        category = request.POST["category"]

        listing = Listing(
            user=user,
            title=title,
            description=description,
            price=float(startingBid),
            imageURL=imageURL,
            category=category,
            numberBids=0
        )
        listing.save()

        return HttpResponseRedirect(reverse("index"))
    elif request.method == "GET":
        return render(request, "auctions/createListings.html", {
            "categories": categories
        })


def categories_(request):
    return render(request, "auctions/categoryMain.html", {
        "categories": categories
    })


def categoriesFiltered(request, category):
    return render(request, "auctions/categoryFiltered.html", {
        "categories": categories,
        "listings": Listing.objects.all(),
        "filterName": category
    })


def listing(request, title):
    item = Listing.objects.get(title=title)

    return render(request, "auctions/listing.html", {
        "title": title,
        "owner": item.owner,
        "description": item.description,
        "price": item.price,
        "wishlisted": wishlisted
    })


def watchlist(request, username, title):
    if request.method == "POST":

        item = Watchlist.objects.filter(user=username, product=title).first()

        if item == None:
            newWatchlist = Watchlist(
                product=title,
                user=username
            )
            newWatchlist.save()
            wishlisted = True

            return HttpResponseRedirect(reverse("listing", kwargs={"title": title}))

        else:
            item.delete()
            wishlisted = False

            return HttpResponseRedirect(reverse("listing", kwargs={"title": title}))
