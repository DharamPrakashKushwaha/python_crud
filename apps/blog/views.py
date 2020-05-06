import json

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializer import PostSerializer
from rest_framework.decorators import api_view


# Create your views here.

class PostAPI(APIView):
    def get(self, request):
        postData = Post.objects.all()
        serialize = PostSerializer(postData, many=True)
        return Response(serialize.data)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        title = data['title']
        body = data['body']
        author = User.objects.get(pk=data['author'])
        p = Post(author=author, title=title, body=body)
        p.save()
        return HttpResponse("Post saved successfully!")

    def patch(self, request):
        data = json.loads(request.body.decode('utf-8'))
        Post.objects.filter(pk=data['post_id']).update(body=data['body'], title=data['title'])
        return HttpResponse("Post Updated successfully!")

    @api_view(['POST'])
    def registration(request):
        # print(request.body)
        registerData = json.loads(request.body.decode('utf-8'))
        first_name = registerData['first_name'];
        last_name = registerData['last_name'];
        username = registerData['username'];
        password = registerData['password'];
        email = registerData['email']

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name= last_name)
        user.save()
        print('saved')
        return HttpResponse(
            'user is registered.'
        );