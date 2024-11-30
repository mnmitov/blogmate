from django.views.generic import ListView

from blog.models import Post


# Create your views here.

class HomePage(ListView):
    template_name = 'common/dashboard.html'
    context_object_name = 'posts'
    model = Post


    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset
