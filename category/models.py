from django.db import models


class Category(models.Model):
    """Model for Category"""
    class Meta:
        """Set verbose name"""
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50, unique=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories/', blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
