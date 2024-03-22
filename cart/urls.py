from django.urls import path
from . import views
from .views import cartView, addToCartView, confirm_order

app_name = 'cart'

urlpatterns = [
    path('add_to_cart/<int:product_id>/', addToCartView, name='add_to_cart'),
    path('', cartView, name='cart'),
    path('confirm-order/', confirm_order, name='confirm_order'),
]
