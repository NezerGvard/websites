from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image

import datetime

class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='название')
    svg = models.CharField(max_length=10000, verbose_name='вектор')
    slug = models.SlugField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=60, verbose_name='название')
    price = models.IntegerField(verbose_name='цена')
    description = models.CharField(max_length=400, verbose_name='описание', blank=True)
    characteristic = models.CharField(max_length=400, verbose_name='характеристика', blank=True)
    image = models.ImageField(upload_to ='uploads/%Y/%m/%d/', verbose_name='изображение')
    category = models.ManyToManyField(Category, verbose_name='категория')
    created = models.DateTimeField(editable=False, verbose_name='создано')
    modified = models.DateTimeField(editable=False, blank=True, verbose_name='изменено')

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        return super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ['category__name']

class Product_basket(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name='товар')
    count = models.IntegerField(verbose_name='количество')

    def __str__(self) -> str:
        return str(self.count)

class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь')
    product = models.ManyToManyField(Product_basket, verbose_name='товар')

    def __str__(self) -> str:
        return str(self.count)

class Sales(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE, verbose_name='категория')
    amount = models.IntegerField(verbose_name="Прибыль")








