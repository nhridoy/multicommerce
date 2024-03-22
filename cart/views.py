from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from product.models import Product
from .models import Cart, Order, CartItem


def cartView(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)


    context = {
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)

@login_required
def addToCartView(request, product_id):
    current_product = get_object_or_404(Product, id=product_id)
    # Check if the user already has a cart
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Try to get the cart item for the product
    cart_item, created = CartItem.objects.get_or_create(product=current_product, cart=cart)

    # If the cart item already exists, increment its quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def confirm_order(request):
    # Retrieve the current user's cart
    cart = Cart.objects.get(user=request.user)

    # Create an Order instance linked to the current user's cart
    order = Order.objects.create(user=request.user, cart=cart)

    # Clear the cart by deleting all CartItem instances
    cart.cart_item_cart.all().delete()

    # Redirect to a success page or back to the cart page
    return redirect('ecommerce:index')