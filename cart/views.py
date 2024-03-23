from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
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
def confirm_order(request):
    # Retrieve the current user's cart
    cart = Cart.objects.get(user=request.user)

    # Create an Order instance linked to the current user's cart
    order = Order.objects.create(user=request.user, cart=cart, revenue=cart.get_total())

    # Clear the cart by deleting all CartItem instances
    cart.cart_item_cart.all().delete()

    # Redirect to a success page or back to the cart page
    return redirect('ecommerce:index')
