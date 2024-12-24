from rest_framework import viewsets, permissions
from .models import User, Product, Category
from .serializers import UserSerializer, ProductSerializer, CategorySerializer
from rest_framework import viewsets, permissions, filters
from .models import User, Product, Category
from .serializers import UserSerializer, ProductSerializer, CategorySerializer
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
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'category__name']
    filterset_fields = ['category']
    ordering_fields = ['name', 'price']
