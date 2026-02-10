# API URLs
from . import api_views

urlpatterns = [
    path('api/products/', api_views.product_list_api, name='api_product_list'),
    path('api/products/<slug:slug>/', api_views.product_detail_api, name='api_product_detail'),
    path('api/collections/', api_views.collection_list_api, name='api_collection_list'),
    path('api/my-orders/', api_views.my_orders_api),
]
