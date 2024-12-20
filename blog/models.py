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
        related_name='authors_posts',
    )

    views = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return f"{self.title} by {self.author}"


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

    author = models.ForeignKey(
        to=AppUser,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Comment: {self.content} by {self.author}"


class Like(models.Model):
    author = models.ForeignKey(
        to=AppUser,
        on_delete=models.CASCADE,
        related_name='author_likes',
    )

    post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
        related_name='post_likes',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Like on post {self.post} by {self.author}"
