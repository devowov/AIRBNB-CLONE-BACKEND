from django.contrib import admin
from .models import Tweet, Like

# Register your models here.
class ElonMuskFilter(admin.SimpleListFilter):
    title = 'Elon Musk'
    parameter_name = 'elon_musk'

    def lookups(self, request, model_admin):
        return (
            ('contains', 'Contains "Elon Musk"'),
            ('not_contain', 'Does not contain "Elon Musk"'),
        )

    def queryset(self, request, tweets):
        if self.value() == 'contain':
            return tweets.filter(payload__icontains='Elon Musk')
        elif self.value() == 'not_contain':
            return tweets.exclude(payload__icontains='Elon Musk')
        return tweets

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user'
                    , 'payload'
                    , 'created_at')
    
    search_fields = ['payload', 'user__username']
    list_filter = ['created_at', ElonMuskFilter]

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user'
                    , 'tweet'
                    , 'created_at')
    search_fields = ['user__username']
    list_filter = ['created_at']