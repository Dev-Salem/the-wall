from datetime import timedelta

from django.db.models import Count
from django.utils import timezone
from rest_framework.response import Response

from .models import Post
from .pagination import CustomCommentPagePagination
from .serializers import CommentSerializer


def paginate_comment_section(post, request):
    comments = post.comment_set.all()
    comment_paginator = CustomCommentPagePagination()
    paginatedComments = comment_paginator.paginate_queryset(
        queryset=comments, request=request
    )
    serialized_comments = CommentSerializer(instance=paginatedComments, many=True)
    return serialized_comments.data, comment_paginator.get_next_link()


def get_popular_posts_queryset():
    last_day = timezone.now() - timedelta(days=1)
    return (
        Post.objects.filter(
            created_at__gte=last_day,
        )
        .annotate(votes=Count("vote"))
        .order_by("-votes", "created_at")
    )
