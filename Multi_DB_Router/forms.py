from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import CustumUser


class AccountCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

class CustomUserForm(forms.ModelForm):

    class Meta:
        model = CustumUser
        fields = ['database1',
                  'database2',
                  'database3',
                  'database4',
                  'database5',]

