from django.shortcuts import render
from .models import FAQ


def faqs(request):
    """ A view to return the FAQs page """
    faqs = FAQ.objects.all()
    template = "faqs/faqs.html"
    context = {
        "faqs": faqs,
    }
    return render(request, template, context)
