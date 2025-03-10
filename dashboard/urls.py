from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [

    # Main
    path('', views.dashboard, name='dashboard'),

    # Module Post 
    path('posts/', views.posts, name='posts'),

    # Module Categories
    path('categories/', views.categories, name='categories'),
    path('categories/create/', views.create_category, name="create_category"),
    path('categories/update/<int:id>', views.update_category, name="update_category"),
    path('categories/delete/<int:id>', views.delete_category, name="delete_category"),

    # Module Tags
    path('tags/', views.tags, name='tags'),
    path('tags/create/', views.create_tag, name="create_tag"),
    path('tags/update/<int:id>', views.update_tag, name="update_tag"),
    path('tags/delete/<int:id>', views.delete_tag, name="delete_tag"),

    # Module Users
    path('users/', views.users, name="users"),
    path('users/create/', views.create_user, name="create_user"),
    path('users/update/<int:id>', views.update_user, name="update_user"),
    path('users/update_password/<int:id>', views.update_password, name="update_password"),
    path('users/delete/<int:id>', views.delete_user, name="delete_user"),
]
