from django.views.generic.edit import DeleteView, UpdateView
from myblog.forms import PostForm, EditForm
from myblog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Category, Post
from django.urls import reverse_lazy


class HomeView(ListView):
    model= Post
    template_name = 'home.html'
    ordering = ['id']
#def home(request):
 #   return render(request, 'home.html' , {})


class ArticleView(DetailView):
    model = Post
    template_name = 'article.html'
    
class AddPost(CreateView):
    model = Post
    template_name = 'add.html'
    form_class = PostForm
      
class CreateCat(CreateView):
    model = Category
    template_name = 'create_cat.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

class UpdateArticleView(UpdateView):
    model = Post
    template_name = 'update.html'
    form_class = EditForm

class DeleteArticleView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')



 