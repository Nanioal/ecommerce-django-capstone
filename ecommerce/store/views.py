from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import User, Product, Category, Review, ProductImage, Wishlist, Order
from .serializers import UserSerializer, ProductSerializer, CategorySerializer, ReviewSerializer, ProductImageSerializer, WishlistSerializer, OrderSerializer

class ProductPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size' 
    max_page_size = 100

class IsAdminOrSelf(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create_user', 'sign_in_user']:
            self.permission_classes = [AllowAny]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAuthenticated, IsAdminOrSelf]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def create_user(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def sign_in_user(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": UserSerializer(user).data
            })

        return Response({"error": "Invalid credentials"}, status=400)

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

class AdminProductViewSet(viewsets.ModelViewSet): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
    permission_classes = [permissions.IsAdminUser] 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter] 
    filterset_fields = {
        'category': ['exact'], 
        'price': ['gte', 'lte'], 
        'stock_quantity': ['gte', 'lte'],
    } 
    search_fields = ['name'] 
    pagination_class = ProductPagination 

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'])
    def my_orders(self, request):
        queryset = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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
