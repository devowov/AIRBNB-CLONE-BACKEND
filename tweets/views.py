from django.shortcuts import render
from .models import Tweet
from django.http import JsonResponse
from .models import Tweet
from django.contrib.auth import get_user_model
from .serializers import TweetSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()

class TweetListAPIView(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserTweetListAPIView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)  # 유저가 존재하지 않으면 404 반환
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Create your views here.
def tweet_list(request):
    tweets = Tweet.objects.all()
    return render(request, 'tweets/tweets_list.html', {'tweets': tweets})

@api_view()
def all_tweet_list(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

@api_view()
def user_tweet_list(request, user_id):
    try:
        user = User.objects.get(pk=user_id) 
    except User.DoesNotExist:
        return JsonResponse(
            {'error': '존재하지 않는 유저 정보 입니다.'}
            , status=status.HTTP_404_NOT_FOUND
        )

    tweets = Tweet.objects.filter(user=user) 
    serializer = TweetSerializer(tweets, many=True)
    
    return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)