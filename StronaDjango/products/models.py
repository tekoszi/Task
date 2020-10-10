from django.db import models


class Product(models.Model):
    shortDescription = models.CharField(max_length=200)
    description = models.TextField(default='This is a default description2')
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    barcode = models.IntegerField()
    quantity = models.IntegerField()
    # details = [shortDescription, description, price, barcode, quantity]
    def __str__(self):
        # return [self.shortDescription, self.description, self.price, self.barcode, self.quantity]
        return self.shortDescription
