from django import forms
from account.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'street_address_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "House number and street name"}),
            'street_address_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Appartment, suite, unit etc: (optional)"}),
        }
