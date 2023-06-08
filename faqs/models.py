from django.db import models


class FAQ(models.Model):
    """FAQs model"""
    question = models.CharField(max_length=250, null=False, blank=False)
    answer = models.TextField(null=False, blank=False)

    class Meta:
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question
