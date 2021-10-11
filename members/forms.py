from members.models import UserProfile
from myblog.models import Profile
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder' : 'email'}))
    first_name = forms.CharField(max_length=50, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'First Name'}))
    last_name = forms.CharField(max_length=50,  widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'Last Name'}))
    
    class Meta:
        model = UserProfile
        fields = ('username','first_name','last_name', 'email','password1','password2')

       
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ('username','password')

    def clean(self):
        if self.is_valid():
            username=self.cleaned_data['username']
            password = self.cleaned_data['password']

            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid username or Password")


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs = {'class': 'form-control', 'placeholder' : 'email'}))
    first_name = forms.CharField(max_length=50, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'First Name'}))
    last_name = forms.CharField(max_length=50,  widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'Last Name'}))
    username = forms.CharField(max_length=50, widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'First Name'}))
    #last_login = forms.CharField(max_length=50,  widget = forms.TextInput(attrs = {'class': 'form-control', 'type' : 'hidden'}))
    #is_superuser = forms.CharField(max_length=50, widget = forms.CheckboxInput(attrs = {'class': 'form-check', 'type' : 'hidden'}))
    #is_stuff = forms.CharField(max_length=50,  widget = forms.CheckboxInput(attrs = {'class': 'form-check', 'type' : 'hidden'}))
    #is_active = forms.CharField(max_length=50, widget = forms.CheckboxInput(attrs = {'class': 'form-check', 'type' : 'hidden'}))
    #date_joined = forms.CharField(max_length=50,  widget = forms.TextInput(attrs = {'class': 'form-control', 'type' : 'hidden'}))
    
    class Meta:
        model = UserProfile
        fields = ('username','first_name','last_name', 'email','password')

