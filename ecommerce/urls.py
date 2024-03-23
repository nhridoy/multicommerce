from django.urls import path
from .views import indexView

app_name = 'ecommerce'

urlpatterns = [
    path('', indexView, name='index'),
]
