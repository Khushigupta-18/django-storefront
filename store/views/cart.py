from django.shortcuts import redirect, render, get_object_or_404
from store.models import Cart, CartItem, Product

def add_to_cart(request, product_id):
    cart_id = request.session.get('cart_id')

    if not cart_id:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    else:
        cart = Cart.objects.get(id=cart_id)

    product = get_object_or_404(Product, id=product_id)

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect('store:product_detail', slug=product.slug)

def view_cart(request):
    cart_id = request.session.get('cart_id')

    if not cart_id:
        return render(request, 'store/cart.html', {
            'items': [],
            'total': 0
        })

    cart = Cart.objects.get(id=cart_id)
    items = cart.items.select_related('product')
    total = sum(i.quantity * i.product.unit_price for i in items)

    return render(request, 'store/cart.html', {
        'items': items,
        'total': total
    })
    
def remove_from_cart(request, item_id):
        cart_id = request.session.get('cart_id')
        if cart_id:
            CartItem.objects.filter(id=item_id, cart_id=cart_id).delete()
            return redirect('store:view_cart')


def update_cart_item(request, item_id, action):
    item = get_object_or_404(CartItem, id=item_id)

    if action == 'increase':
        item.quantity += 1
        item.save()
    elif action == 'decrease':
        item.quantity -= 1
        if item.quantity <= 0:
            item.delete()
        else:
            item.save()

    return redirect('store:view_cart')



