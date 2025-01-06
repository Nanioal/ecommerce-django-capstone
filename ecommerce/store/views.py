from rest_framework import viewsets, permissions, filters
from .models import User, Product, Category, Review, ProductImage, Wishlist,  Order
from .serializers import UserSerializer, ProductSerializer, CategorySerializer, ReviewSerializer, ProductImageSerializer,  WishlistSerializer, OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import serializers, viewsets, permissions
from rest_framework.pagination import PageNumberPagination



class ProductPagination(PageNumberPagination):
     page_size = 10 
     page_size_query_param = 'page_size' 
     max_page_size = 100

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Allow unauthenticated access to the create action
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        'category': ['exact'],
        'price': ['gte', 'lte'],
        'stock_quantity': ['gte', 'lte'],
    }
    search_fields = ['name']
    pagination_class = ProductPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Product does not exist.")
        except Exception as e:
            raise serializers.ValidationError(str(e))


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
