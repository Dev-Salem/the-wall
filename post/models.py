import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q


class UserGeneratedContent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.CharField(
        max_length=300,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        abstract = True


class Post(UserGeneratedContent):
    pass


class Comment(UserGeneratedContent):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )


class Vote(models.Model):
    VOTE_TYPE = (
        ("up", "Upvote"),
        ("down", "Downvote"),
    )
    vote = models.CharField(max_length=4, choices=VOTE_TYPE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "author",
                    "post",
                ],
                name="each user can vote each post just once",
                violation_error_message="Already voted on this post",
            ),
            models.UniqueConstraint(
                fields=[
                    "author",
                    "comment",
                ],
                name="each user can vote each comment just once",
                violation_error_message="Already voted on this comment",
            ),
            models.CheckConstraint(
                name="Either post is null or comment is null",
                check=Q(post__isnull=True, comment__isnull=False)
                | Q(post__isnull=False, comment__isnull=True),
                violation_error_message="You can vote either a post or a comment",
            ),
        ]

    def __str__(self):
        if self.post:
            return f"{self.vote} on '{self.post}' by {self.author}"
        else:
            return f"{self.vote} on '{self.comment}' by {self.author}"
