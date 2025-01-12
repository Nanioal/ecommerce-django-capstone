from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib import admin
from .models import Product, Category, Order, Wishlist
from .models import Review
admin.site.register(User, UserAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity')
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'comment', 'created_at')
    search_fields = ('product__name', 'user__username', 'rating', 'comment')
    list_filter = ('product', 'user', 'rating', 'created_at')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('user', 'product', 'created_at')

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('user', 'product', 'created_at')

# Register your models here.
