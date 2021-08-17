from django.urls import path
from .views import ApiOverView, ShowAllPost

urlpatterns = [
    
    path('', ApiOverView, name="api" ),
    path('post-list/', ShowAllPost, name="show-all"),

]