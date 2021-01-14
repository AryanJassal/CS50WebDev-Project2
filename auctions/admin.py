from django.contrib import admin

from .models import Listing, Comment, Watchlist, Bid, Categories, User


class BidAdmin(admin.ModelAdmin):
    list_display = ['listing', 'amount', 'user']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'user', 'listing']


class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'closed']


class WatchlistAdmin(admin.ModelAdmin):
    list_display = ['listing', 'user']


admin.site.register(Watchlist, WatchlistAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Categories)
admin.site.register(User)
