from members.views import UserEditView, UserRegisterView
from django.urls import path, include
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('edit_profile/',UserEditView.as_view(), name = 'edit_profile' ),
]