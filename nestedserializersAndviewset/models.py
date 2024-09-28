from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Phone(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, related_name='phones', on_delete=models.CASCADE)


    def __str__(self):
        return self.name
