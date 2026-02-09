from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    #products
    path('products/', views.product_list, name='product_list'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    #collections
    path('collections/', views.collection_list, name='collection_list'),
    path('collections/<int:id>/', views.collection_detail, name='collection_detail'),
    #cart
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/<str:action>/', views.update_cart_item, name='update_cart_item'),
    #checkout
    path('checkout/', views.checkout, name='checkout'),
]





