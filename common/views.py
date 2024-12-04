from django.db.models import Count
from django.views.generic import ListView
from blog.models import Post


# Create your views here.



class HomePage(ListView):
    template_name = 'common/dashboard.html'
    context_object_name = 'posts'
    model = Post

    def get_queryset(self):
        return self.model.objects.annotate(likes_count=Count('post_likes'))

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['is_author'] = self.request.user == self.object_list.author
    #     return context