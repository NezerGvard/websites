from django.urls  import path

from .views import *
urlpatterns = [
    path('', index),
    path("product/<int:product_id>/", get_product),
    path("register", register, name="register"),
    path("login", user_login, name="login"),
    path("logout", user_logout, name="logout"),
    path("register-telegram/<str:username>/<str:password>/<str:email>", register_telegram)
]