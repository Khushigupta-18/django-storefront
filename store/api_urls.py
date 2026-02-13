from django.urls import path
from . import api_views

urlpatterns = [
    path('products/', api_views.product_list_api),
    path('products/<slug:slug>/', api_views.product_detail_api),
    path('collections/', api_views.collection_list_api),
    path('my-orders/', api_views.my_orders_api),
]
