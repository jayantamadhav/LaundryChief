from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class SignUpForm(UserCreationForm):
    #full_name = forms.CharField(max_length=100, help_text='Required. 100 charaters of fewer.')
    first_name = forms.CharField(max_length=30, required=False, help_text='Enter First name')
    last_name = forms.CharField(max_length=30, required=False, help_text='Enter Last name')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ( 'first_name', 'last_name', 'age', 'email', 'password1', 'password2')

