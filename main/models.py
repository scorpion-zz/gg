from django.db import models

class AdditionalCarImage(models.Model):
    image = models.ImageField(upload_to='car_image', blank=True, null=True)
    car = models.ForeignKey('Car',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.car.brand} {self.car.model}'

class Car(models.Model):
    brand = models.ForeignKey("Brand",on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    manufacturer = models.ManyToManyField('Manufacture')
    image = models.ImageField(upload_to='car_image', blank=True, null=True)

    def __str__(self):
        return f'{self.brand} {self.model}'

class Brand(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Manufacture(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


