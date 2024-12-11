from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from BlogMate.mixins import TitleMixin
from account.forms import CustomUserForm, CustomLoginForm, ProfileEditForm
from account.models import AppUser, Profile


# Create your views here.
class CustomRegisterView(TitleMixin, CreateView):
    form_class = CustomUserForm
    template_name = 'registration/register.html'
    title = 'Registration'
    success_url = reverse_lazy('login')


class CustomLoginView(TitleMixin, LoginView):
    template_name = 'registration/login.html'
    title = 'Login'
    form_class = CustomLoginForm
    success_url = reverse_lazy('homepage')


class AccountDetails(TitleMixin, DetailView):
    template_name = 'account/profile.html'
    title = 'Your account'
    model = Profile

    def get_object(self, queryset=None):
        user = self.kwargs['pk']
        if user:
            return Profile.objects.get(user=user)
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        if not profile:
            raise Http404('The profile you are looking for does not exist')
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_object()
        context['profile_owner'] = self.request.user.id == self.kwargs['pk']
        return context


class EditAccountView(TitleMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    title = 'Edit Account'
    template_name = 'account/edit.html'
    model = Profile
    form_class = ProfileEditForm

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

    def test_func(self):
        profile = self.get_object()
        return profile.user == self.request.user

    def handle_no_permission(self):
        return redirect('forbidden-page')

    def get_success_url(self):
        return reverse_lazy('account-details', kwargs={'pk': self.object.user.pk})


class DeleteAccountView(TitleMixin, LoginRequiredMixin, DeleteView):
    template_name = 'account/delete.html'
    title = 'Delete Account'
    success_url = reverse_lazy('homepage')
    model = AppUser

    def get_object(self, queryset=None):
        return self.request.user

    def handle_no_permission(self):
        return redirect('forbidden-page')
