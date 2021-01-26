from django.urls import path,include
from Farmer import views
urlpatterns = [
    path('',views.home,name='home'),
    path('product',views.product,name='product'),
    path('peptisides',views.pept,name='peptisides'),
    path('insctiside',views.insect,name='insctiside'),
    path('contactus',views.contact,name='contactus'),
    path('cust_registration',views.cust_reg,name='cust_registration'),
    path('cust_login',views.login,name='cust_login'),
    path('farmer_home',views.farmer_home,name='farmer_home'),
    path('farmer_product',views.farmer_product,name='farmer_product'),
    path('farmer_pept',views.farmer_pept,name='farmer_pept'),
    path('farmer_insect',views.farmer_insect,name='farmer_insect'),
    path('farmer_cart',views.farmer_cart,name='farmer_cart'),
    path('farmer_info',views.farmer_info,name='farmer_info'),
    path('farmer_notification',views.farmer_notfi,name='farmer_notification'),
    path('farmer_order',views.farmer_order,name='farmer_order'),
    path('farmer_track',views.farmer_track,name='farmer_track')
]