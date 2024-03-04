from django.db import models
from django.contrib.auth.models import User
import uuid

class Shop(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name='owned_shops', on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    shop = models.ForeignKey(Shop, related_name='food_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, related_name='orders', on_delete=models.CASCADE)
    items = models.ManyToManyField(FoodItem, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('CONFIRMED', 'Confirmed'), ('READY', 'Ready')])
    waiting_time = models.IntegerField(help_text="Estimated waiting time in minutes", null=True, blank=True)
    confirmation_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

def generate_uuid():
    return uuid.uuid4().hex

class OTP(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, default=generate_uuid, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP {self.code} for Order {self.order.id}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
