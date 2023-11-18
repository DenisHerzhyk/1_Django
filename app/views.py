from django.shortcuts import render, redirect, get_object_or_404
from .models import Product


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']

        product = Product(name=name, description=description, price=price)
        product.save()

    return render(request, 'index.html')


def display(request):
    products = Product.objects.all()
    return render(request, 'display.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']

        product = Product(name=name, description=description, price=price)
        product.save()

        return redirect('display')

    return render(request, 'index.html')


def delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()

    return redirect('display')
