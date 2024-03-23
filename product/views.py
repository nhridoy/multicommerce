from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets, views, generics, pagination, response, permissions, status

# Create your views here.
from .forms import ProductForm
from .models import Product
from .serializers import ProductSerializer


def inventoryView(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    products = Product.objects.filter(seller=request.user)

    context = {
        'products': products,
        'form': form
    }
    return render(request, 'inventory.html', context)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
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
