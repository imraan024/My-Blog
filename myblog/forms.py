from django import forms
from django.forms import widgets 
from .models import Post, Category

choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author', 'category','body')

        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'Give a Title'}),
            'author': forms.TextInput(attrs = {'class': 'form-control', 'value' : '', 'id': 'imran', 'type':'hidden'}),
            #'author': forms.Select(attrs = {'class': 'form-control'}),
            'category': forms.Select(choices = choice_list, attrs = {'class': 'form-control'}),
            'body': forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Write your Artcle here'})


        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body')

        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control', 'placeholder' : 'Give a Title'}),
            'body': forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Write your Artcle here'})
        }