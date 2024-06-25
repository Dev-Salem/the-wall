import logging

from rest_framework import filters, permissions, viewsets, mixins
from rest_framework.exceptions import NotFound

from . import utils
from .models import Comment, Post, Vote
from .pagination import CustomPagePagination
from .permissions import isAuthorOrReadOnly
from .serializers import *

logger = logging.getLogger(__name__)


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [isAuthorOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagePagination
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = [
        "body",
    ]
    ordering_fields = [
        "created_at",
    ]
    ordering = [
        "-created_at",
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        obj = super().retrieve(request, *args, **kwargs)
        obj.data["comments"], obj.data["next_comments_page"] = (
            utils.paginate_comment_section(self.get_object(), request)
        )
        return obj


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [isAuthorOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CustomPagePagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class VoteViewSet(viewsets.ModelViewSet):
    permission_classes = [isAuthorOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class PopularPostsListView(viewsets.generics.ListAPIView):
    queryset = utils.get_popular_posts_queryset()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    pagination_class = CustomPagePagination


class RepliesListView(viewsets.generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CustomPagePagination

    def get_queryset(self):
        queryset = super().get_queryset()
        comment_id = self.kwargs["id"]
        comment = Comment.objects.get(id=comment_id)
        if comment_id is not None:
            queryset = comment.comment_set.all()
            return queryset
        else:
            raise NotFound
