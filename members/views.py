from django.contrib.auth.views import PasswordChangeView
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .forms import  SignUpForm, EditProfileForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from myblog.models import Profile

class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswodrsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('home')


class ProfilePageView(DetailView):
    model = Profile 
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
        context["page_user"] = page_user
        return context
class EditProfilePageView(UpdateView):
    model = Profile
    template_name = "registration/edit_profile_page.html"
    success_url = reverse_lazy('home')
    fields = ['bio','profile_pic']