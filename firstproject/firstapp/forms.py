from django import forms
from firstapp.models import users

class NewUser(forms.ModelForm):
    class Meta:
        model = users
        fields = '__all__'
