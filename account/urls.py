from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from account.views import CustomRegisterView, AccountDetails, CustomLoginView, EditAccountView, DeleteAccountView

urlpatterns = [
    path('<int:pk>/', include([
        path('', AccountDetails.as_view(), name='account-details'),
        path('edit/', EditAccountView.as_view(), name='account-edit'),
        path('delete/', DeleteAccountView.as_view(), name='account-delete')
    ])),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(next_page='homepage'), name='login'),
    path('logout/', LogoutView.as_view(next_page='homepage'), name='logout'),
]