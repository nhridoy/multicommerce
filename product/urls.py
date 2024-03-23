from django.urls import path, include
from . import views
from rest_framework import routers
from .views import inventoryView, ProductViewSet

app_name = 'product'

router = routers.DefaultRouter()
router.register(r'', ProductViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path("", ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('inventory', inventoryView, name='inventory'),
]
