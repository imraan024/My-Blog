from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import PostSerializer
from myblog.models import Post
# Create your views here.


@api_view(['GET'])
def ApiOverView(request):
    api_urls = {
        'List': '/post-list/',

    }

    return Response(api_urls)

@api_view(['GET'])
def ShowAllPost(request):
    posts = Post.objects.filter(post_status = 1)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

