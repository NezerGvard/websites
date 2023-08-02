from django.urls import path
from .views import *

urlpatterns = [
    path('', Product_view.as_view(), name='product_list'),
    path('cart/', Basket_view.as_view(), name='cart'),
    path('sales/', Sales_response.as_view(), name='sales'),
    path('login/', User_login.as_view(), name='login'),
    path('logout/', User_logout.as_view(), name='logout'),
    path('report/', Report.as_view(), name='report'),
    path('register/', User_register.as_view(), name='register'),
    path('category/<str:slug_name>', Product_category.as_view(), name='slug'),
    path('product/<int:product_id>', Get_product.as_view(),  name='product'),
    path('cart/delete/product=<int:product_id>', Delete_basket.as_view(), name='delete_cart'),
    path('category/<str:slug_name>/add/cart/product=<int:product_id>&count=<int:count>', Add_basket.as_view(), name='add_cart' ),
    path('update/cart/product=<int:product_id>&count=<int:count>/', Update_basket.as_view(), name='update_cart' ),
]

