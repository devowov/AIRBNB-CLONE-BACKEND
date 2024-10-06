from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.Serializer):
    user = serializers.StringRelatedField()  # 유저를 username으로 표시하기 위해 설정

    class Meta:
        model = Tweet
        fields = ['id', 'payload', 'created_at', 'user']  # 모델의 필드를 자동으로 직렬화
    # id = serializers.IntegerField()
    # payload = serializers.CharField(max_length=280)
    # created_at = serializers.DateTimeField()
    # user = serializers.CharField(source='user.username')

    # def create(self, validated_data):
    #     return Tweet.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.payload = validated_data.get('payload', instance.payload)
    #     instance.save()
    #     return instance