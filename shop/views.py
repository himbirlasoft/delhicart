from django.shortcuts import render
from .models import Product,Contact
from django.http import HttpResponse
from math import ceil

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('categoty', 'id')
    cats = {item['categoty'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(categoty=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request,'shop/about.html')
def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()        
    return render(request,'shop/contact.html')
def tracker(request):
    return HttpResponse("I am in tracker")
def search(request):
    return HttpResponse("I am in search")
def prodView(request):
    return HttpResponse("I am in prodView")
def checkout(request):
    return HttpResponse("I am in checkout")



# Create your views here.
