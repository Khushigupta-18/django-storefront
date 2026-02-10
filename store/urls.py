from django.urls import path
from store.views.products import product_list, product_detail
from store.views.collections import collection_list, collection_detail
from store.views.cart import add_to_cart, view_cart, remove_from_cart, update_cart_item
from store.views.checkout import checkout

app_name = 'store'

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('products/<slug:slug>/', product_detail, name='product_detail'),

    path('collections/', collection_list, name='collection_list'),
    path('collections/<int:id>/', collection_detail, name='collection_detail'),

    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/<str:action>/', update_cart_item, name='update_cart_item'),

    path('checkout/', checkout, name='checkout'),
]
