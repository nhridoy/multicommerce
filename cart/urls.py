from django.urls import path
from . import views
from .views import cartView, confirm_order

app_name = 'cart'

urlpatterns = [
    path('', cartView, name='cart'),
    path('confirm-order/', confirm_order, name='confirm_order'),
]
