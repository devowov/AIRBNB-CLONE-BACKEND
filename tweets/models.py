from django.db import models
from common.models import CommomModel

# Create your models here.
class Tweet(CommomModel):
    payload = models.TextField(max_length = 180)
    user = models.ForeignKey("users.User"
                            , on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Tweet by {self.user.username}: "{self.payload[:50]}"'

class Like(CommomModel):
    user = models.ForeignKey("users.User"
                            , on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet
                              , on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} liked Tweet: "{self.tweet.payload[:50]}"'