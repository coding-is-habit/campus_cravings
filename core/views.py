# core/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth import login as auth_login, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Shop, FoodItem, Order


def landing_page(request):
    return render(request, 'landing_page.html')

# User Registration View

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def signup_login(request):
    action = request.GET.get('action', 'login')

    # Initialize form variable based on the action parameter
    if action == 'register':
        form = UserCreationForm()
    else:
        form = AuthenticationForm()

    if request.method == 'POST':
        if 'login' in request.POST:
            # Create a new instance of the login form with the POST data
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('core:landing_page')  # Redirect to a home page or other target
        elif 'register' in request.POST:
            # Create a new instance of the registration form with the POST data
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('core:landing_page')  # Redirect to a home page or other target

    return render(request, 'login.html', {'form': form, 'action': action})
# Shop Listing View
class ShopListView(ListView):
    model = Shop
    template_name = 'shops/list.html'
    context_object_name = 'shops'
    queryset = Shop.objects.all().order_by("-id")

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
