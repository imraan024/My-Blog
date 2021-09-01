from .views import CreateProfilePageView, ProfilePageView, UserEditView,  PasswodrsChangeView, EditProfilePageView, UserRegisterView
from django.urls import path
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('edit_profile/',UserEditView.as_view(), name = 'edit_settings'),
    path('password/', PasswodrsChangeView.as_view()),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name ='profile_page'),
    path('<int:pk>/edit_profile', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name = 'create_profile'),
]