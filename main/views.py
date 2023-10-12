from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from main.models import Product

# Create your views here.
def index_page(request):
    message = 'ПРИВЕТ ВСЕМ!'
    return  HttpResponse(message)

def products_list(request):
    products = Product.objects.all()
    template_name = 'main/list.html'
    #return HttpResponse(products)
    return render(request, template_name, {'products':products})

def product_details(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    tamplate_name = 'main/details.html'
    return render(request, tamplate_name, {'item':product})