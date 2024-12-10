from django.db.models import Count
from django.views.generic import ListView, TemplateView

from blog.models import Post


# Create your views here.

class HomePage(ListView):
    template_name = 'common/dashboard.html'
    context_object_name = 'posts'
    model = Post
    paginate_by = 3

    def get_queryset(self):
        return self.model.objects.annotate(likes_count=Count('post_likes')).order_by('-date_added')



class ForbiddenPage(TemplateView):
    template_name = 'common/403.html'
