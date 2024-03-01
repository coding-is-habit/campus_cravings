# core/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Shop, FoodItem, Order


def landing_page(request):
    return render(request, 'landing_page.html')

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('core:shop_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Shop Listing View
class ShopListView(ListView):
    model = Shop
    template_name = 'shops/list.html'
    context_object_name = 'shops'

# Shop Detail View
class ShopDetailView(DetailView):
    model = Shop
    template_name = 'shops/detail.html'
    context_object_name = 'shop'

# Food Item Listing View
def food_item_list(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    food_items = FoodItem.objects.filter(shop=shop)
    return render(request, 'food_items/list.html', {'shop': shop, 'food_items': food_items})

# User Order Listing View
@login_required
def user_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-id')
    return render(request, 'orders/list.html', {'orders': orders})
