from django.contrib import admin
from .models import (
    Product,
    Collection,
    Customer,
    Order,
    OrderItem,
    Cart,
    CartItem,
    Promotion,
    Address
)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'unit_price', 'inventory', 'last_update')
    list_filter = ('collection',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'membership')
    list_filter = ('membership',)
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'placed_at', 'payment_status')
    list_filter = ('payment_status',)
