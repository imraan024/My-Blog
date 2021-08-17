from django.urls import path
from .views import ApiOverView, ShowAllPost

urlpatterns = [
    
    path('', ApiOverView, name="api" ),
    path('list/', ShowAllPost, name="show-all"),

]