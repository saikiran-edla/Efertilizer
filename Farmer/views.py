from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def product(request):
    return render(request,'products.html')
def pept(request):
    return render(request,'peptiside.html')
def insect(request):
    return render(request,'insectiside.html')
def contact(request):
    return render(request,'contactus.html')
def cust_reg(request):
    return render(request,'customer.html')
def login(request):
    return render(request,'farmer login.html')
def farmer_home(request):
    return render(request,'farmerhome.html')
def farmer_product(request):
    return render(request,'farmerproducts.html')
def farmer_pept(request):
    return render(request,'farmerpesticide.html')
def farmer_insect(request):
    return render(request,'farmerinsctiside.html')
def farmer_cart(request):
    return render(request,'farmercart.html')
def farmer_info(request):
    return render(request,'farmerinfo.html')
def farmer_notfi(request):
    return render(request,'farmernotification.html')
def farmer_order(request):
    return render(request,'farmerorders.html')
def farmer_track(request):
    return render(request,'trackyourorder.html')