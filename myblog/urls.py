from django.urls import path
#from . import views
from .views import AddPost, ArticleView, HomeView, RegisterView
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name = "article"),
    path('add', AddPost.as_view(), name = "add_post"),
    path('register', RegisterView.as_view(), name = "register"),
]