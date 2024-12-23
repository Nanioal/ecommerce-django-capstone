from rest_framework import viewsets, permissions
from .models import User, Product, Category
from .serializers import UserSerializer, ProductSerializer, CategorySerializer
from rest_framework import viewsets, permissions, filters
from .models import User, Product, Category, Review
from .serializers import UserSerializer, ProductSerializer, CategorySerializer, ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend


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

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
class ReviewViewSet(viewsets.ModelViewSet): 
    queryset = Review.objects.all() 
    serializer_class = ReviewSerializer 
    permission_classes = [permissions.IsAuthenticated] 
    def perform_create(self, serializer): 
        serializer.save(user=self.request.user)
