from django.db import models


# Create your models here.
class Box(models.Model):
    Id = models.CharField(max_length=50, primary_key=True)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Zip_code = models.IntegerField()
    Latitude = models.DecimalField(max_length=10, max_digits=25, decimal_places=10)
    Longitude = models.DecimalField(max_length=10, max_digits=25, decimal_places=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address
