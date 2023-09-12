from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message, Chat

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'phone_number', 'password')  # Include any additional fields you need

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'sender', 'recipient', 'content', 'timestamp')  # Include any additional fields you need


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'