# Uncomment the following imports before adding the Model code

from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    SUV = "SUV"
    SEDAN = "SEDAN"
    WAGON = "WAGON"

    CAR_TYPE_CHOICES = {
        SUV: "SUV",
        SEDAN: "Sedan",
        WAGON: "Wagon",
    }

    dealer_id = models.IntegerField(null=True)
    name = models.CharField(max_length=255, null=False)
    type = models.CharField(choices=CAR_TYPE_CHOICES, default=SUV)
    year = models.IntegerField(null=False, default=2026,
        validators=[
            MaxValueValidator(2027),
            MinValueValidator(2015)
        ]
    )
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
