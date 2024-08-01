from rest_framework import serializers
from main.models import Manufacture

class BrandSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

class ManufactureSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    model = serializers.CharField()
    price = serializers.DecimalField(max_digits=8,decimal_places=2)
    description =serializers.CharField()
    image = serializers.ImageField()
    brand = BrandSerializer()
    manufacturer = ManufactureSerializer(many=True)

class ManufacturerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Manufacture
        fields = '__all__'

    def create(self, validated_data):
        return Manufacture.objects.create(**validated_data)