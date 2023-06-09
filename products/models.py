from django.db import models
from django.core.validators import MaxValueValidator


class Category(models.Model):
    """Model for Category"""
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    cat_image = models.ImageField(null=True, blank=True)

    class Meta:
        """Set verbose name"""
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """Model for Product"""
    name = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)  # noqa
    description = models.TextField()
    estimated_dispatch = models.CharField(max_length=254, null=True, blank=True)  # noqa
    price = models.IntegerField(validators=[MaxValueValidator(99999)], null=False, blank=False)  # noqa
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # noqa
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
