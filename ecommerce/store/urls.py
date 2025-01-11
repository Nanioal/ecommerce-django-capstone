from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, CategoryViewSet,ReviewViewSet 
from .views import ProductViewSet, ProductImageViewSet, WishlistViewSet, OrderViewSet, AdminProductViewSet



router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'products', ProductViewSet, basename='product') 
router.register(r'admin/products', AdminProductViewSet, basename='admin-product')
router.register(r'orders', OrderViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'product-images', ProductImageViewSet)
router.register(r'wishlists', WishlistViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

                                                                                                                                                                   

