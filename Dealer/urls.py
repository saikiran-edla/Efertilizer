from django.urls import path,include
from Dealer import views
urlpatterns = [
    path('',views.SellLogin,name='Sellerlogin'),
    path('seller_reg',views.SellReg,name='seller_reg'),
    path('Dealer_home',views.Home,name='Dealer_home'),
    path('Addproduct',views.Add_Product,name='Addproduct'),
    path('Update_product',views.Update,name='Update_product'),
    path('Dealer_info',views.Dealer_info,name='Dealer_info'),
    path('Delivery',views.Deliver,name="Delivery"),
    path('OrderRecived',views.Order_Reciver,name='OrderRecived')
]