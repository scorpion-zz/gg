from django.urls import path

from main.views import (page_add_car,get_page_1,detail_info,get_brand,
                        get_search,get_registration,autoriz,logaut_user,kabinet,my_orders)

urlpatterns = [
    path('',get_page_1,name='home'),
    path('add_car/',page_add_car,name='add_car'),
    path('detail/<int:id>/',detail_info,name='detail_info'),
    path('brand/',get_brand,name='brand'),
    path('search/',get_search,name='search'),
    path('registration/',get_registration,name='registration'),
    path('autoriz/',autoriz,name='autoriz'),
    path('logaut',logaut_user,name='logaut'),
    path('kabinet',kabinet,name='kabinet'),
    path('my_orders',my_orders,name='my_orders'),
]