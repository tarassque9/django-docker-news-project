from django.shortcuts import get_object_or_404
from .models import Post

from django.db.models import F


def _change_post_vote(operation: str, pk: int) -> bool:
    """Incremet or decrement post vote"""
    post = get_object_or_404(Post, pk=pk)
    if operation == 'increment':
        Post.objects.filter(id=post.id).update(votes=F('votes') + 1)
        return True
    elif operation == 'decrement':
        Post.objects.filter(id=post.id).update(votes=F('votes') - 1)
        return True
    else:
        return False


def _null_votes():
    """null all post votes"""
    posts = Post.objects.all()
    for post in posts:
        post.votes = 0
        post.save()
