from django.contrib.auth.views import PasswordChangeView
from django.urls.base import reverse
from django.views.generic import View, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .forms import  SignUpForm, EditProfileForm
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from myblog.models import Profile

#views

class UserRegisterView(CreateView):
    form_class = SignUpForm
    print(type(form_class))
    template_name = 'registration/register.html'
        



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

class CreateProfilePageView(CreateView):
    model = Profile
    template_name = "registration/create_user_profile.html"
    fields = ('bio','profile_pic')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)