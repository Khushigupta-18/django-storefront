from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer

#product list api
@api_view(['GET', 'POST'])
def product_list_api(request):
    
 #GET → List Products
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

# POST → Create Product
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

#product detail api(slug)
@api_view(['GET', 'POST', 'DELETE'])
def product_detail_api(request, slug):
    
    product = get_object_or_404(Product, slug=slug)
# GET → Single Product
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

# PUT → Update Product
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE → Remove Product
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

#collection list api
@api_view(['GET'])
def collection_list_api(request):
    collections = Collection.objects.all()
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_orders_api(request):
    orders = Order.objects.filter(customer=request.user)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

