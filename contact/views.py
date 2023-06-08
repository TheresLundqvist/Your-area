from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


def contact(request):
    """ A view to return the contact page """
    contact_form = ContactForm(request.POST or None)
    if request.method == "POST":
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Successfully sent your message!")
            return redirect("home")
    template = "contact/contact.html"
    context = {
        "form": contact_form,
    }
    return render(request, template, context)
