from django import forms
from .models import Order


class PlaceOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['citizenName', 'contact', 'address', 'paidAmount']
