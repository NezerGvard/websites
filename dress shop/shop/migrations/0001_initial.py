# Generated by Django 4.1.1 on 2022-10-23 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='название')),
                ('image', models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='изображение')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='цена')),
                ('description', models.CharField(blank=True, max_length=400, verbose_name='описание')),
                ('characteristic', models.CharField(blank=True, max_length=400, verbose_name='характеристика')),
                ('image', models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='изображение')),
                ('created', models.DateTimeField(editable=False, verbose_name='создано')),
                ('modified', models.DateTimeField(blank=True, editable=False, verbose_name='изменено')),
                ('category', models.ManyToManyField(to='shop.category', verbose_name='категория')),
            ],
        ),
        migrations.CreateModel(
            name='Product_basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='количество')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='товар')),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ManyToManyField(to='shop.product_basket', verbose_name='товар')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]
