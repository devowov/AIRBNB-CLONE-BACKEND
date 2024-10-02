from django.shortcuts import render
from .models import Tweet

# Create your views here.
def tweet_list(request):
    tweets = Tweet.objects.all()
    return render(request, 'tweets/tweets_list.html', {'tweets': tweets})