from myblog.forms import PostForm
from myblog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class HomeView(ListView):
    model= Post
    template_name = 'home.html'
#def home(request):
 #   return render(request, 'home.html' , {})


class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'
    
class AddPost(CreateView):
    model = Post
    template_name = 'add.html'
    form_class = PostForm
    #fields = '__all__'
class RegisterView(CreateView):
    model = Post
    template_name = 'register.html'

 