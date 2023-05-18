from django.db import models


class Product(models.Model):
    """Model for Product"""
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    estimated_dispatch = models.CharField(max_length=254, null=True, blank=True)  # noqa
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # noqa
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
