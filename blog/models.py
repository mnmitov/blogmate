from django.contrib.auth.models import User
from django.db import models

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

    author = models.CharField(
        max_length=30
    )


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.CharField(
        max_length=100,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )