from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import ProductCreateForm

def index(request):
    context = {
        'allobjects': Product.objects.all()
    }
    return render(request, 'Products/index.html', context)
    # return HttpResponse("Hello, world. You're at the products index.")

def detail(request, product_id):
    return HttpResponse("You're looking at product %s." % product_id)

def new(request):
    context = {
    }

    # if request.method == 'POST':
    #     print(request.POST)
    #     shortDescription = request.POST.get('Short Description')
    #     description = request.POST.get('Description')
    #     price = request.POST.get('Price')
    #     barcode = request.POST.get('Barcode')
    #     quantity = request.POST.get('Quantity')
    #     print(shortDescription,description,price,quantity,barcode)
    #     Product.objects.create(shortDescription=shortDescription, description=description, price=price, barcode=barcode, quantity=quantity)
    return render(request, 'Products/new.html', context)

# def new(request):
#     form = ProductCreateForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductCreateForm()
#     context = {
#         'form': form
#     }
#
#     return render(request, 'Products/new.html', context)

# Create your views here.
