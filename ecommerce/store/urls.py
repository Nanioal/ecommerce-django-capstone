# store/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, CategoryViewSet, ProductViewSet,ProductImageViewSet, AdminProductViewSet,
    OrderViewSet, ReviewViewSet, WishlistViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'admin/products', AdminProductViewSet, basename='admin-products')
router.register(r'orders', OrderViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'product-images', ProductImageViewSet)
router.register(r'wishlists', WishlistViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include the router-generated routes
    path('create-order/<int:pk>/', OrderViewSet.as_view({'post': 'create_order'}), name='create_order'),
]
