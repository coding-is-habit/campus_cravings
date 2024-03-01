# urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import landing_page, register

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
