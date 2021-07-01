from members.views import UserRegisterView
from django.urls import path, include
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
]