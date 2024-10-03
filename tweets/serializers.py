from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    payload = serializers.CharField(max_length=280)
    created_at = serializers.DateTimeField()
    user = serializers.CharField(source='user.username')

    def create(self, validated_data):
        return Tweet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.payload = validated_data.get('payload', instance.payload)
        instance.save()
        return instance