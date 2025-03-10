from django.urls import path
from . import views

app_name = "accounts_security"

urlpatterns = [
    path('', views.signin_page, name="signin_page"),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name="signout")
]
