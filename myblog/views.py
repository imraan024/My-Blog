from django.views.generic.edit import DeleteView, UpdateView
from .forms import PostForm, EditForm
from .models import Post, Category
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class HomeView(ListView):
    model= Post
    template_name = 'home.html'
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
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

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category = cats)
    return render(request, 'categories.html', { 'cats': cats, 'category_posts' : category_posts })

