from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    """
        Form to allow users to sign-up for newsletter
    """
    class Meta:
        model = Newsletter
        fields = "__all__"
