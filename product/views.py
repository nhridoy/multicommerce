from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets, views, generics, pagination, response, permissions, status, exceptions

# Create your views here.
from rest_framework.generics import get_object_or_404
from cart.models import CartItem, Cart
from .forms import ProductForm
from .models import Product
from .serializers import ProductSerializer


def inventoryView(request):
    form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'inventory.html', context)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('pk')
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.user_type == 'seller':
                return self.queryset.filter(seller=self.request.user)
        return self.queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(seller=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def add_to_cart(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            raise exceptions.NotAuthenticated
        product = get_object_or_404(self.queryset, id=kwargs.get('id'))
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)

        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return response.Response({"detail": f"{product.name} added to cart. Total = {cart_item.quantity}"})
