from rest_framework import serializers
from . import models


class MySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=15)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyUser
        fields = ('id', 'name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        new_user = models.MyUser.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return new_user


class FeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FeedItem
        fields = ('id', 'status', 'profile', 'date')
        extra_kwargs = {
            'profile': {'read_only': True}
        }