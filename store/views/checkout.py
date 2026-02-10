from django.shortcuts import redirect, render
from store.models import Cart, Order, OrderItem

def checkout(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        return redirect('store:product_list')

    cart = Cart.objects.get(id=cart_id)
    items = cart.items.all()

    if not items:
        return redirect('store:product_list')

    order = Order.objects.create(
        customer=request.user,
        payment_status=Order.PAYMENT_STATUS_PENDING
    )

    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            unit_price=item.product.unit_price
        )

    items.delete()
    del request.session['cart_id']

    return render(request, 'store/checkout_success.html', {
        'order': order
    })
