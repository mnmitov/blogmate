from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from account.forms import CustomUserForm, CustomUserChangeForm
from account.models import Profile, AppUser


# Create your views here.
class UserRegisterView(CreateView):
    form_class = CustomUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('homepage')


class AccountDetails(UpdateView):
    template_name = 'account/profile.html'
    form_class = CustomUserChangeForm
    model = AppUser
    success_url = reverse_lazy('homepage')



