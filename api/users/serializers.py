from django.contrib.auth import authenticate, get_user_model
from djoser.conf import settings
# from djoser.serializers import TokenCreateSerializer
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from api.users.models import *

User = get_user_model()


class NeuralDropTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeuralDropTasks
        fields = "__all__"



class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'username', 'password', 'company', 'industry']
