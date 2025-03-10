from django.urls import path
from . import views

app_name = "web_blog"

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:id>', views.view_post, name='view_post'),
]
