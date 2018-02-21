from django.contrib.auth.models import User
from .models import Purchase
from django import forms

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['address',]
