from django.shortcuts import render, get_object_or_404
from store.models import Collection

def collection_list(request):
    collections = Collection.objects.all()
    return render(request, 'store/collection_list.html', {
        'collections': collections
    })

def collection_detail(request, id):
    collection = get_object_or_404(Collection, id=id)
    products = collection.products.all()
    return render(request, 'store/collection_detail.html', {
        'collection': collection,
        'products': products
    })
