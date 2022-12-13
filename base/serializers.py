from rest_framework import serializers

class MySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=15)
