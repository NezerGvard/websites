# Generated by Django 4.1.1 on 2022-10-23 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='svg',
            field=models.CharField(default=2, max_length=3000, verbose_name='вектор'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='цена'),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField(verbose_name='скидка')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='товар')),
            ],
        ),
    ]
