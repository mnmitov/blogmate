from django.urls import path
from blog.views import AddBlog, EditBlog

urlpatterns = [
    path('add_blog/', AddBlog.as_view(), name='add-topic'),
    path('edit_blog/', EditBlog.as_view(), name='edit-topic'),
]