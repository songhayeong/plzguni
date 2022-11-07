from django.contrib.auth import authenticate, get_user_model
from djoser.conf import settings
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from api.users.models import *

User = get_user_model()


class NeuralDropTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeuralDropTasks
        fields = "__all__"



class UserSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'company']


class TestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingTasks
        fields = "__all__"



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__" 


class RecommendedTech1Serializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedTech1
        fields = "__all__"      


class RecommendedTech2Serializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedTech2
        fields = "__all__"        


class RecommendedTech3Serializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedTech3
        fields = "__all__"        


class RecommendedTech4Serializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedTech4
        fields = "__all__"


class RecommendedTech5Serializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedTech5
        fields = "__all__"        


class RecommendedTech6Serializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedTech6
        fields = "__all__"             


class ResultTechSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultTech
        fields = "__all__"


class AiSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingAiModel
        fields = "__all__"


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"        