from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list') # '/' 경로에 뷰 연결
    , path('tweets/', views.all_tweet_list, name='all_tweet_list') # Tweets 리스트
    , path('users/<int:user_id>/tweets/', views.user_tweet_list, name='user_tweet_list') # User 가 만든 모든 Tweets 리스트 
]