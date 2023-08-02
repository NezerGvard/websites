from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import *

class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget(), label='описание')
    characteristic = forms.CharField(widget=CKEditorUploadingWidget(), label='характеристика')
    class Meta:
        model = Product
        fields = '__all__'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ("name", )}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ['name', 'price', 'image_show', 'created', 'modified']
    list_filter = ['created', 'modified']
    list_editable = ['price']
    # prepopulated_fields = {'slug': ('name', )}

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = "Картинка"
