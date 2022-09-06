import djoser
from djoser import urls
from djoser.urls import jwt
from djoser.urls import authtoken
from django.urls import path
from django.conf.urls import include
from api.users import views
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
# from rest_framework.urlpatterns import format_suffix_patterns


app_name = "users"
urlpatterns = [
    path("testing/", include(djoser.urls)),
    #path("testing/", include(djoser.urls.authtoken)),
    path("testing/", include(djoser.urls.jwt)),
    #path("words/", views.testingapi.as_view()),
    path("NeuralDrops/", views.NeuralDropViewsets.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path("NeuralDrops/<int:pk>", views.NeuralDropViewsets.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),

]


