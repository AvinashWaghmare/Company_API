from django.contrib import admin
from django.urls import path, include
from api.views import UserViewSet, PostViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('',include(router.urls))
]