from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from blog.forms import BlogCreateForm, BlogEditForm, BlogDetailsForm, BlogDeleteForm
from blog.models import Post

# Create your views here.


class AddBlogPost(CreateView):
    template_name = 'blog/add_blog.html'
    form_class = BlogCreateForm
    model = Post
    success_url = reverse_lazy('homepage')


class EditBlogPost(UpdateView):
    template_name = 'blog/edit_blog.html'
    form_class = BlogEditForm
    success_url = reverse_lazy('article')
    model = Post


class DeleteBlogPost(DeleteView):
    template_name = 'blog/delete_blog.html'
    form_class = BlogDeleteForm
    success_url = reverse_lazy('homepage')
    model = Post

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)



class ArticleView(DetailView):
    template_name = 'blog/article.html'
    context_object_name = 'article'
    form_class = BlogDetailsForm
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_author'] = self.request.user == self.get_object().author
        return context


    # def get_queryset(self):
    #     queryset = self.model.objects.all()
    #     return queryset

    def get_queryset(self):
        return self.model.objects.annotate(likes_count=Count('post_likes'))


    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context




