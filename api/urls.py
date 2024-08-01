from django.urls import path

from api.views import get_car_list, manufacturer, SearchProduct

urlpatterns = [
    path('get_car_list/',get_car_list),
    path('manufacturer/',manufacturer),
    path('search_product/',SearchProduct.as_view()),
    ]