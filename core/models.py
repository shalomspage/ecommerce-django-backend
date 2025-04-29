from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    imageUrl = models.URLField(blank=True,)

    class Meta:
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.title
    
class Brand(models.Model):
    title = models.CharField(max_length=100, unique=True)
    imageUrl = models.URLField(blank=False)

    class Meta:
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField(default=0, blank=False)
    description = models.TextField(max_length=500)
    is_featured = models.BooleanField(default=False)
    clothesType = models.CharField(max_length=250, default=title)
    ratings = models.FloatField(blank=False, default=1.0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    colors = models.JSONField(blank=True)
    sizes = models.JSONField(blank=True)
    imageUrl = models.JSONField(blank=True)
    created_at = models.DateTimeField(default=timezone.now, blank=False)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title
    
