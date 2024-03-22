from django.urls import path
from . import views
from .views import inventoryView

app_name = 'product'

urlpatterns = [
    path('inventory', inventoryView, name='inventory'),
]
