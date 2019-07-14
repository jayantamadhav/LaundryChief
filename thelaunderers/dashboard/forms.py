from django import forms
from django.forms import ModelForm
from .models import Customer


class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ('cust_name', 'cust_email', 'cust_phone', 'cust_address', )