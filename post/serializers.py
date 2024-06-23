from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Comment, Post, Vote


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "profile_image"]


class PostSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "body",
            "created_at",
            "author",
            "upvotes_count",
            "downvotes_count",
            "comments_count",
        ]
        read_only_fields = ["author"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["author"]


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"
        read_only_fields = ["author"]
