import json

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializer import CommentSerializer
from rest_framework.decorators import api_view


# Create your views here.
from ..blog.models import Post


class CommentAPI(APIView):
    def get(self, request):
        commentData = Comment.objects.all()
        serialize = CommentSerializer(commentData, many=True)
        return Response(serialize.data)

    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        comment = data['comment']
        user_id = User.objects.get(pk=data['user_id'])
        post_id = Post.objects.get(pk=data['post_id'])
        p = Comment(comment=comment, user_id=user_id, post_id=post_id)
        p.save()
        return HttpResponse("Comment saved successfully!")

    def patch(self, request):
        data = json.loads(request.body.decode('utf-8'))
        Comment.objects.filter(pk=data['comment_id']).update(comment=data['comment'])
        return HttpResponse("Comment Updated successfully!")
