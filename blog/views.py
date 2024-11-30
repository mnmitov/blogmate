from django.shortcuts import render
from django.views.generic import CreateView, UpdateView


# Create your views here.

class AddBlog(CreateView):
    template_name = 'blog/add_blog.html'


class EditBlog(UpdateView):
    template_name = 'blog/edit_blog.html'

