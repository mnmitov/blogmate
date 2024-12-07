from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from BlogMate.mixins import TitleMixin
from blog.forms import BlogCreateForm, BlogEditForm, BlogDeleteForm, CommentCreateForm
from blog.models import Post, Like, Comment


# Create your views here.


class AddBlogPost(TitleMixin, LoginRequiredMixin, CreateView):
    template_name = 'blog/add_blog.html'
    title = 'Create Blog Post'
    form_class = BlogCreateForm
    model = Post
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditBlogPost(TitleMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'blog/edit_blog.html'
    form_class = BlogEditForm
    title = 'Edit blog post'
    model = Post

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    def get_success_url(self):
        return reverse_lazy('article', kwargs={'pk': self.object.pk})

    def handle_no_permission(self):
        return redirect('forbidden-page')



class DeleteBlogPost(TitleMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'blog/delete_blog.html'
    title = 'Delete blog post'
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



class ArticleView(TitleMixin, DetailView):
    template_name = 'blog/article.html'
    context_object_name = 'article'
    title = 'Article'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-created_at')
        if self.request.user.is_authenticated:
            context['is_author'] = self.request.user == self.get_object().author
            context['user_liked'] = self.get_object().post_likes.filter(author=self.request.user).exists()
        context['likes_count'] = self.get_object().post_likes.count()

        return context

    def get_object(self, queryset = None):
        if not hasattr(self, '_object'):
            self._object = super().get_object(queryset)
            self._object.views += 1
            self._object.save(update_fields=['views'])
        return self._object



class LikesView(View):

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        like, created = Like.objects.get_or_create(post=post, author=request.user)
        if not created:
            like.delete()
            liked = False
        else:
            liked = True

        likes_count = post.post_likes.count()
        return JsonResponse({'liked': liked, 'likes_count': likes_count})


class AddCommentView(TitleMixin, LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'blog/comments/add-comment.html'
    title = 'Add comment'

    def handle_no_permission(self):
        return redirect('forbidden-page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        # print(Post.objects.get(pk=self.kwargs['pk']))
        # print(super().form_valid(form))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article', kwargs={'pk': self.kwargs['pk']})






