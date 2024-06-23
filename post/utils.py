from rest_framework.response import Response

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
