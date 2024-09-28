from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.ForeignKey(Type, related_name='vehicles', on_delete=models.CASCADE)


    def __str__(self):
        return self.name
