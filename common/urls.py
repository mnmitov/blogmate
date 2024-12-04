from django.urls import path

from common.views import ForbiddenPage, HomePage

urlpatterns = [
    path('forbidden/', ForbiddenPage.as_view(), name='forbidden-page'),
    path('', HomePage.as_view(), name='homepage'),
]