# core/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'core'  # Namespace for the 'core' app

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login/', views.signup_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('shops/', views.ShopListView.as_view(), name='shop_list'),
    path('shops/<int:pk>/', views.ShopDetailView.as_view(), name='shop_detail'),
    path('shops/<int:shop_id>/food_items/', views.food_item_list, name='food_item_list'),
    path('my_orders/', views.user_orders, name='user_orders'),
]
