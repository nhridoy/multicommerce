from django.urls import path
from .views import inventoryView, ProductViewSet

app_name = 'product'

urlpatterns = [
    # path('', include(router.urls)),
    path("", ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("add-to-cart/<int:id>/", ProductViewSet.as_view({'get': 'add_to_cart'})),
    path('inventory', inventoryView, name='inventory'),
]
