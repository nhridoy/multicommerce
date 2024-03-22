from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from .forms import ProductForm
from .models import Product


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
