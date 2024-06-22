from django.contrib import admin

from .models import *


class CommentInline(admin.TabularInline):
    model = Comment


class VoteInline(admin.TabularInline):
    model = Vote


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline, VoteInline]


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Vote)
