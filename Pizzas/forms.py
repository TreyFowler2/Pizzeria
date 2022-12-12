from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','email']
        labels = {'first_name':'First Name',
                    'last_name':'Last Name',
                    'email':'Email'}
