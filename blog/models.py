from django.contrib.auth.models import User
from django.db import models

from account.models import AppUser


# Create your models here.

class Post(models.Model):
    TITLE_MAX_LENGTH = 300

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )

    description = models.TextField()

    date_added = models.DateTimeField(
        auto_now_add=True
    )

    date_modified = models.DateTimeField(
        auto_now=True
    )

    author = models.ForeignKey(
        to=AppUser,
        on_delete=models.CASCADE,
        related_name='authors',
    )


class Comment(models.Model):
    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    content = models.CharField(
        max_length=1000,
        default='',
    )

    author = models.OneToOneField(
        to=AppUser,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )


class Like(models.Model):
    like = models.BooleanField(
        default=False,
    )

    author = models.ForeignKey(
        to=AppUser,
        on_delete=models.CASCADE,
        related_name='author_likes',
    )

    post = models.OneToOneField(
        to=Post,
        on_delete=models.CASCADE,
        related_name='post_likes',
    )
