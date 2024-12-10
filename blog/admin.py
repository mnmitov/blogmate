from django.contrib import admin

from blog.models import Post, Comment, Like


# Register your models here.

@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ['title', 'author', 'date_added', 'date_modified', 'views']
    list_filter = ['title', 'author', 'date_added', 'date_modified', 'views']
    ordering = ('-date_added', '-date_modified')
    list_per_page = 10
    list_display_links = ['title', 'author']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['content']
    list_display = ['post', 'author', 'content', 'created_at']
    list_filter = ['post', 'author', 'content', 'created_at']
    ordering = ('-created_at',)
    list_per_page = 10
    list_display_links = ['post', 'author', 'content']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at']
    list_filter = ['author', 'post', 'created_at']
    ordering = ('-created_at',)
    list_per_page = 10
    list_display_links = ['author', 'post']
