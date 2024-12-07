from django.urls import path, include
from blog.views import AddBlogPost, EditBlogPost, DeleteBlogPost, ArticleView, LikesView, AddCommentView

urlpatterns = [
    path('add-article/', AddBlogPost.as_view(), name='add-article'),
    path('<int:pk>/', include([
        path('edit-article/', EditBlogPost.as_view(), name='edit-article'),
        path('delete-article/', DeleteBlogPost.as_view(), name='delete-article'),
        path('article/', ArticleView.as_view(), name='article'),
        path('like/', LikesView.as_view(), name='like_post'),
        path('add-comment/', AddCommentView.as_view(), name='add-comment'),
    ])),
]
