from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, CartViewSet, CartItemViewSet, OrderViewSet, DailyDataViewSet,indexView

app_name = 'ecommerce'
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cartitems', CartItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'dailydata', DailyDataViewSet)

urlpatterns = [
    path('', indexView, name='index'),


    path('', include(router.urls)),
]
