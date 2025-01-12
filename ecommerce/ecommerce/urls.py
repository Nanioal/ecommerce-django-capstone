from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.views import UserViewSet, CategoryViewSet, ProductViewSet, AdminProductViewSet, OrderViewSet, ReviewViewSet, ProductImageViewSet, WishlistViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'admin/products', AdminProductViewSet, basename='admin-products')
router.register(r'orders', OrderViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'product-images', ProductImageViewSet)
router.register(r'wishlists', WishlistViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
