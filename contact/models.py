from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=30)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name
