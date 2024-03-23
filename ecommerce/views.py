from django.shortcuts import render
from rest_framework import viewsets
from .models import DailyData
from product.models import Product
from cart.models import Cart, CartItem
from user.models import User

from .serializers import UserSerializer, ProductSerializer, CartSerializer, CartItemSerializer, OrderSerializer, DailyDataSerializer

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from cart.models import Order


def indexView(request):
    page_number = request.GET.get('page', 1)
    paginator = Paginator(Product.objects.all(), 12)
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
    }
    return render(request, 'index.html', context)

class RegisterView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        data = request.data
        name = data['name']
        email = data['email'].lower()
        password = data['password']
        re_password = data['re_password']
        user_type = data['user_type']

        if password != re_password:
            return Response({'error': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'User with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(name=name, email=email, password=password, user_type=user_type)
        return Response({'success': 'User created successfully.'}, status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class DailyDataViewSet(viewsets.ModelViewSet):
    queryset = DailyData.objects.all()
    serializer_class = DailyDataSerializer
