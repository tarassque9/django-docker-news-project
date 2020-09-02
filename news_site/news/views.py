from .models import Author, Post, Comment
from .serializers import AuthorSerializer, PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .services import _change_post_vote


class AuthorModelViewSet(viewsets.ModelViewSet):
    """All actions to Author model:
    read - GET method
    create - POST method
    partial update - PATCH method
    update all fields - PUT method
    delete - DELETE method
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PostModelViewSet(viewsets.ModelViewSet):
    """All actions to Post model"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentModelViewSet(viewsets.ModelViewSet):
    """All actions to Comment model"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpvotesPostView(APIView):
    """Decrement current post votes in 1"""
    def post(self, request, pk, format=None):
        if _change_post_vote('decrement', pk):
            return Response({'status': True})
        Response({'status': False})


class VotesPostView(APIView):
    """Increment current post votes in 1"""
    def post(self, request, pk, format=None):
        if _change_post_vote('increment', pk):
            return Response({'status': True})
        Response({'status': False})
