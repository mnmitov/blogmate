from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from BlogMate.mixins import TitleMixin
from account.forms import CustomUserForm, CustomUserChangeForm
from account.models import Profile, AppUser


# Create your views here.
class UserRegisterView(TitleMixin, CreateView):
    form_class = CustomUserForm
    template_name = 'registration/register.html'
    title = 'Registration'
    success_url = reverse_lazy('homepage')


class AccountDetails(TitleMixin, UpdateView):
    template_name = 'account/profile.html'
    form_class = CustomUserChangeForm
    title = 'Your account details'
    model = AppUser
    success_url = reverse_lazy('homepage')



