from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from blog.forms import BlogCreateForm, BlogEditForm, BlogDetailsForm, BlogDeleteForm
from blog.models import Post

# Create your views here.


class AddBlogPost(CreateView, LoginRequiredMixin):
    template_name = 'blog/add_blog.html'
    form_class = BlogCreateForm
    model = Post
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditBlogPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'blog/edit_blog.html'
    form_class = BlogEditForm
    model = Post

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    def get_success_url(self):
        return reverse_lazy('article', kwargs={'pk': self.object.pk})

    def handle_no_permission(self):
        return redirect('forbidden-page')



class DeleteBlogPost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'blog/delete_blog.html'
    form_class = BlogDeleteForm
    success_url = reverse_lazy('homepage')
    model = Post

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    def handle_no_permission(self):
        return redirect('forbidden-page')


    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)



class ArticleView(LoginRequiredMixin, DetailView):
    template_name = 'blog/article.html'
    context_object_name = 'article'
    form_class = BlogDetailsForm
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = self.request.user == self.get_object().author
        return context

    def get_object(self, queryset = None):
        if not hasattr(self, '_object'):
            self._object = super().get_object(queryset)
            self._object.views += 1
            self._object.save(update_fields=['views'])
        return self._object

    def get_queryset(self):
        return self.model.objects.annotate(likes_count=Count('post_likes'))




