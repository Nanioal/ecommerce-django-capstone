from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.product.stock_quantity -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)
        
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image_url = models.URLField()

    def __str__(self):
        return f"Image for {self.product.name}"

class Review(models.Model): 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews') 
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)]) 
    comment = models.TextField() 
    created_date = models.DateTimeField(auto_now_add=True) 
    class Meta: 
        unique_together = ('product', 'user')

class Wishlist(models.Model): 
    user = models.ForeignKey(User, related_name='wishlists', on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, related_name='wishlists', on_delete=models.CASCADE) 
    added_date = models.DateTimeField(auto_now_add=True) 
    def __str__(self): 
        return f"{self.user.username}'s wishlist"
    

# Create your models here.
