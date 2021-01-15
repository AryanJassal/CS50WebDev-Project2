from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import User, Listing, Comment, Watchlist, Bid, Categories
from .forms import LoginForm, RegisterForm, CreateListing


def index(request):
    return render(request, 'auctions/index.html', {
        'listings': Listing.objects.filter(closed=False),
        'heading': 'Active Listings'
    })


def login_(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'auctions/login.html', {
                'form': LoginForm,
                'errors': ['Invalid username and/or password.']
            })
    elif request.method == 'GET':
        return render(request, 'auctions/login.html', {
            'form': LoginForm()
        })


def logout_(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        email = 'someone@emailprovider.com'
        errors = []

        if len(form.data.get('username')) > 24:
            errors.append('The username is too long.')

        if len(form.data.get('password')) < 6:
            errors.append('The password is too short.')

        if form.data.get('password') != form.data.get('confirmPassword'):
            errors.append('The passwords do not match.')

        if User.objects.get(username=form.data.get('username')).exists():
            errors.append('A user with this username already exists.')

        if errors:
            return render(request, 'auctions/register.html', {
                'errors': errors,
                'form': RegisterForm(initial={'username': form.data.get('username')})
            })

        user = User.objects.create_user(username=form.data.get('username'), email=email, password=form.data.get('password'))
        user.save()

        login(request, user)
        return redirect('index')
    elif request.method == 'GET':
        return render(request, 'auctions/register.html', {
            'form': RegisterForm()
        })


@login_required
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        startingBid = request.POST.get('startingBid')
        imageURL = request.POST.get('imageURL')
        categoryList = request.POST.getlist('category')

        errors = []
        if len(description) > 2500:
            errors.append('The description cannot be longer than 2500 characters.')
        elif len(description) <= 0:
            errors.append('The description is too short.')
        if len(title) <= 0:
            errors.append('The title is too short.')
        elif len(title) > 200:
            errors.append('The title cannot be longer than 200 characters.')

        if errors:
            return render(request, 'auctions/create_listings.html', {
                'form': CreateListing(request.POST),
                'categories': Categories.objects.all(),
                'errors': errors
            })

        if imageURL == '':
            imageURL = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/600px-No_image_available.svg.png'

        if len(description) > 255:
            iDescription = description[0:255] + '...'
        else:
            iDescription = description

        item = Listing(
            owner=request.user,
            title=title,
            description=description,
            indexDescription=iDescription,
            price=float(startingBid),
            imageURL=imageURL,
        )
        item.save()

        for i in categoryList:
            item.categories.add(Categories.objects.get(slug=i))

        item.save()

        return redirect('index')
    elif request.method == 'GET':
        return render(request, 'auctions/create_listings.html', {
            'form': CreateListing(),
            'categories': Categories.objects.all()
        })


def categories(request):
    return render(request, 'auctions/category.html', {
        'categories': Categories.objects.all()
    })


def categoriesFiltered(request, slug):
    return render(request, 'auctions/index.html', {
        'listings': Listing.objects.filter(closed=False, categories=Categories.objects.get(slug=slug)),
        'heading': Categories.objects.get(slug=slug).name
    })


def listing(request, pk):
    item = Listing.objects.get(pk=pk)

    if request.user.is_authenticated:
        try:
            wishlisted = Watchlist.objects.get(listing=item, user=request.user)
        except Watchlist.DoesNotExist:
            wishlisted = None
    else:
        wishlisted = None

    try:
        price = Bid.objects.filter(listing=item).first().amount
    except AttributeError:
        price = item.price

    try:
        currentBidder = Bid.objects.filter(listing=item).first().user
    except AttributeError:
        currentBidder = 'No one'

    return render(request, 'auctions/listing.html', {
        'listing': item,
        'price': price,
        'wishlisted': wishlisted,
        'comments': Comment.objects.filter(listing=item),
        'numberBids': item.bid_set.all().count(),
        'currentBidder': currentBidder,
    })


@login_required
def displayWatchlist(request):
    entries = Watchlist.objects.filter(user=request.user)
    listings = []

    if entries is not None:
        for entry in entries:
            listings.append(entry.listing)

    return render(request, 'auctions/watchlist.html', {
        'listings': listings
    })


@login_required
def watchlist(request, pk):
    if request.method == 'POST':
        item = Listing.objects.get(pk=pk)

        watch = Watchlist.objects.filter(user=request.user, listing=item).first()

        if watch is None:
            newWatchlist = Watchlist(
                listing=item,
                user=request.user
            )
            newWatchlist.save()

            return redirect('listing', pk=pk)

        else:
            watch.delete()

            return redirect('listing', pk=pk)


@login_required
def bid(request, pk):
    if request.method == 'POST':
        amount = request.POST.get('amount')

        item = Listing.objects.get(pk=pk)

        try:
            price = Bid.objects.filter(listing=item).first().amount
        except AttributeError:
            price = item.price

        if price > float(amount):
            try:
                wishlisted = Watchlist.objects.get(listing=item, user=request.user)
            except Watchlist.DoesNotExist:
                wishlisted = None

            try:
                price = Bid.objects.filter(listing=item).first().amount
            except AttributeError:
                price = item.price

            try:
                currentBidder = Bid.objects.filter(listing=item).first().user
            except AttributeError:
                currentBidder = 'No one'

            return render(request, 'auctions/listing.html', {
                'listing': item,
                'price': price,
                'wishlisted': wishlisted,
                'comments': Comment.objects.filter(listing=item),
                'numberBids': item.bid_set.all().count(),
                'currentBidder': currentBidder,
                'message': 'The bid must be greater than the current highest bid.'
            })
        else:
            newBid = Bid(
                user=request.user,
                listing=item,
                amount=round(float(amount), 2)
            )
            newBid.save()

        return redirect('listing', pk=item.pk)


@login_required
def closeBid(request, pk):
    if request.method == 'POST':
        item = Listing.objects.get(pk=pk)
        item.closed = True
        item.save()

        try:
            currentBidder = Bid.objects.filter(listing=item).first().user
        except AttributeError:
            currentBidder = None

        try:
            price = Bid.objects.filter(listing=item).first().amount
        except AttributeError:
            price = item.price

        return render(request, 'auctions/listing.html', {
            'title': item.title,
            'currentBidder': currentBidder,
            'price': price,
            'pk': pk,
            'closed': True
        })


@login_required
def comment(request, pk):
    if request.method == 'POST':
        item = Listing.objects.get(pk=pk)

        newComment = Comment(
            listing=item,
            user=request.user,
            comment=request.POST.get('comment')
        )
        newComment.save()

        return redirect('listing', pk=item.pk)
