from django.shortcuts import render
from rest_framework import viewsets
from api.models import User, Post
from api.serializers import UserSerializer, PostSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True,methods=['get'])
    def posts(self,request,pk=None):
        try:

            post=Post.objects.get(pk=pk)
            user=User.objects.filter(post=post)
            user_serializer=UserSerializer(user,many=True,context={'request':request})
            return Response(user_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'User might not exist !! Error'
            })

            pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = ['title','body','author']
    pagination_class = LimitOffsetPagination
    #throttle_classes = [UserRateThrottle,AnonRateThrottle]




