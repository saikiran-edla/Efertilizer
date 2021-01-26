from django.shortcuts import render

# Create your views here.
def SellLogin(request):
    return render(request,'sellerlogin.html')
def SellReg(request):
    return render(request,'seller reg.html')
def Home(request):
    return render(request,'dealerhome.html')
def Add_Product(request):
    return render(request,'addproduct.html')
def Update(request):
    return render(request,'update.html')
def Dealer_info(request):
    return render(request,'Dealerinfo.html')
def Deliver(request):
    return render(request,'Deliverystatus.html')
def Order_Reciver(request):
    return render(request,'orderreciverd.html')

