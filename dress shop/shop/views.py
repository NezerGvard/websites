from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt
from django.views import View
 
from .models import *
from .forms import *



class Product_view(View):
    def get(self, request):
        return render(request, 'shop/product/main.html')


class Get_product(View):

    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        slug_name = product.category.all()[0].slug
        return render(request, 'shop/product/product.html', {'product': product, 'slug_name': slug_name})


class Basket_view(View):

    def get(self, request):
        user = request.user
        basket = []
        if user.is_authenticated == False:
            return redirect('/')
        if Basket.objects.filter(user=user).exists():
            for i in Basket.objects.get(user=user).product.all():
                product = Product.objects.get(id=i.product_id)
                basket.append({'basket': product, 'count': i.count, 'price': i.count*product.price})
            return render(request, 'shop/product/basket.html', {'basket': basket})
        else:
            return render(request, 'shop/product/basket.html', {'error': True})
        
    @csrf_exempt
    def post(self, request):
        user = request.user
        if Basket.objects.filter(user=user).exists():
            basket = Basket.objects.get(user=user)
            product = basket.product.all()
            product.delete()
            basket.delete()
        return redirect(f'/cart')


class Sales_response(View):
    def get(self, request):
        user = request.user
        sales = Sales.objects.filter 

        if user.is_authenticated == False:
            return redirect('/')
        if Basket.objects.filter(user=user).exists():
            for i in Basket.objects.get(user=user).product.all():
                product = Product.objects.get(id=i.product_id)
                category = product.category.all()[0]
                if sales(category = category).exists():
                    temp = sales(category = category)
                    amount = temp[0].amount + product.price * i.count
                    temp.update(amount = amount)
                else:
                    Sales.objects.create(category = category, amount = product.price * i.count).save()
        else:
            return redirect(f'/cart')

        if Basket.objects.filter(user=user).exists():
            basket = Basket.objects.get(user=user)
            product = basket.product.all()
            product.delete()
            basket.delete()
        return redirect(f'/cart')

class Report(View):
    def get(self, request):
        return render(request, 'shop/product/report.html', {'sales': Sales.objects.all()})

class Product_category(View):

    def get(self, request, slug_name):
        categorys = Category.objects.all()
        category = Category.objects.get(slug = slug_name)
        products = Product.objects.all().filter(category=category.id)
        
        return render(request, 'shop/product/list.html', {'product': products, 'category': categorys, 'name_category': category.name, "slug": slug_name})


class Add_basket(View):

    def get(self, request, slug_name, product_id, count):
        user = request.user
        if user.is_authenticated == False:
            return redirect('/')
        product = Product.objects.get(id=product_id)

        if Product_basket.objects.filter(product=product).exists():
            temp = Product_basket.objects.filter(product=product)
            temp.update(product = product, count = count)
    
            pb = Product_basket.objects.get(product=product)
        else:
            pb = Product_basket.objects.create(product = product, count = count)

        if Basket.objects.filter(user=user).exists():
            basket = Basket.objects.get(user=user)
            basket.save()
            basket.product.add(pb.id)
        else:
            basket = Basket.objects.create(user=user)
            basket.save()
            basket.product.add(pb.id)

        return redirect(f'/category/{slug_name}')



class Update_basket(View):

    def get(self, request, product_id, count):
        product = Product.objects.get(id=product_id)

        if Product_basket.objects.filter(product=product).exists():
            temp = Product_basket.objects.filter(product=product)
            temp.update(product = product, count = count)
            return redirect(f'/cart')


class Delete_basket(View):
    
    def get(self, request, product_id):
        user = request.user
        basket = Basket.objects.get(user=user)
        product = basket.product.filter(product=product_id)
        product.delete()
        return redirect(f'/cart')


class User_logout(View):

    def get(self, request):
        logout(request)
        return redirect('/login')


class User_login(View):

    def get(self, request):
        form = UserLoginForm()
        return render(request, 'shop/authorization/login.html', {'form': form})

    @csrf_exempt
    def post(self, request):
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login/')
    


class User_register(View):
    def get(self, request):
        form = UserRegister()
        return render(request, 'shop/authorization/register.html', {'form': form})
    
    @csrf_exempt
    def post(self, request):
        form = UserRegister(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')


        

