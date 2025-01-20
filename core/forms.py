from django.forms import forms
from core.models import Contact


class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {}