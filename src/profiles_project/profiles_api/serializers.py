
from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializing name field for testing our ApiView"""
    name = serializers.CharField(max_length= 10)
