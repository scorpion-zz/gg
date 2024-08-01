from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.serializers import CarSerializer, ManufacturerSerializers, BrandSerializer
from main.models import Car, Manufacture, Brand


# Create your views here.


@api_view(['GET','POST'])
def get_car_list(request):
    cars =Car.objects.all()
    serializer = CarSerializer(cars,many=True)
    print(request.data)
    return Response(serializer.data)

@api_view(['GET','POST'])
def manufacturer(request):
    manufacturer_queriset = Manufacture.objects.all()
    serializer = ManufacturerSerializers(manufacturer_queriset,many=True)
    if request.method == 'POST':
        serializer = ManufacturerSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return Response(serializer.data)


class SearchProduct(ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        data = self.request.query_params
        queryset = Car.objects.filter(brand__title__icontains=data.get('brand'))
        return queryset
