from django.db import models

# Create your models here.

class Product(models.Model):
    price = models.IntegerField()
    title = models.CharField(max_length=150)
    context = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/product")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['title']

class Order(models.Model):
    product_by = models.JSONField()
    id_buyer = models.IntegerField()
    address = models.CharField(max_length=150)
    total_price = models.IntegerField()
    byt_at = models.DateTimeField(auto_now_add=True)
    paid_for = models.BooleanField(default=False, blank=True)

    def __int__(self):
        return self.id_buyer

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['byt_at']
    

