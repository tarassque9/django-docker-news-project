from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AuthorModelViewSet, PostModelViewSet, CommentModelViewSet,\
                    UpvotesPostView, VotesPostView


router = DefaultRouter()
router.register(r'author', AuthorModelViewSet, basename='author')
router.register(r'post', PostModelViewSet, basename='post')
router.register(r'comment', CommentModelViewSet, basename='comment')
router_urlpatterns = router.urls

urlpatterns = [
    path('upvotes/<int:pk>/', UpvotesPostView.as_view()),
    path('votes/<int:pk>/', VotesPostView.as_view())
] + router_urlpatterns
