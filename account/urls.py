from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from account.views import UserRegisterView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(next_page='homepage'), name='login'),
    path('logout/', LogoutView.as_view(next_page='homepage'), name='logout'),
]