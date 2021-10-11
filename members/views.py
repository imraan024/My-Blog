from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls.base import reverse
from django.views.generic import View, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from members.models import UserProfile
from .forms import  SignUpForm, EditProfileForm, UserLoginForm
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect, redirect
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from myblog.models import Profile
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages

#views
        

     
    

        

    
def register(request):
    context = {}
    form = SignUpForm(request.POST)
    
    if request.POST:
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            
            try:
                username = request.POST.get('username')
                email = request.POST.get('email')
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                #phone = request.POST.get('phone')
                password = request.POST.get('password1')
                print(email)
                #auth_token = str(uuid.uuid4())
                profile_obj = UserProfile.objects.create(username = username, email = email, first_name = first_name, last_name = last_name )
                profile_obj.set_password(password)
                profile_obj.save()
                #print(auth_token)
                #sendMailAfterRagistration(email, auth_token)   
                return redirect("login")      

            except Exception as e:
                print(e)
        context['register_form']=form

    else:
        form=SignUpForm()
        
        context['register_form']=form
        print(context)
    
    return render(request, 'registration/register.html', context)
        
def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'login_form': form,
    }
    return render(request, "registration/login.html", context)

def logout_view(request):
    logout(request)
    return redirect('login')

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
    model = UserProfile 
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
        context["page_user"] = page_user
        return context

class EditProfilePageView(UpdateView):
    model = UserProfile
    template_name = "registration/edit_profile_page.html"
    success_url = reverse_lazy('home')
    fields = ['bio','profile_pic']

class CreateProfilePageView(CreateView):
    model = UserProfile
    template_name = "registration/create_user_profile.html"
    success_url = reverse_lazy('home')
    fields = ('bio','profile_pic')
    def form_valid(self, form):
        form.instance.username = self.request.user
        form.instance.email = self.request.user
        return super().form_valid(form)