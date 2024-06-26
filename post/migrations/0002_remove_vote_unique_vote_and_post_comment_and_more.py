# Generated by Django 5.0.6 on 2024-06-22 13:08

import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='vote',
            name='unique vote and post/comment',
        ),
        migrations.RemoveConstraint(
            model_name='vote',
            name='Either post is null or comment is null',
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.UUIDField(default=uuid.UUID('aca50026-36cc-410f-b55c-83a163d47ebc'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('aca50026-36cc-410f-b55c-83a163d47ebc'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddConstraint(
            model_name='vote',
            constraint=models.UniqueConstraint(fields=('author', 'post', 'vote'), name='each user can vote each post just once', violation_error_message='Already voted on this post'),
        ),
        migrations.AddConstraint(
            model_name='vote',
            constraint=models.UniqueConstraint(fields=('author', 'comment', 'vote'), name='each user can vote each comment just once', violation_error_message='Already voted on this comment'),
        ),
        migrations.AddConstraint(
            model_name='vote',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('comment__isnull', False), ('post__isnull', True)), models.Q(('comment__isnull', True), ('post__isnull', False)), _connector='OR'), name='Either post is null or comment is null', violation_error_message='You can vote either a post or a comment'),
        ),
    ]
