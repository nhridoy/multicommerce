from django.db import models
from product.models import Product
from user.models import User


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_cart")

    def get_total(self):
        total = 0
        for item in self.cart_item_cart.all():
            total += item.product.price * item.quantity
        return total


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_item_product")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_item_cart")
    quantity = models.PositiveIntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    revenue = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
