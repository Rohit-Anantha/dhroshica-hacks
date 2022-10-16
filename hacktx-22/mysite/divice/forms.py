from django import forms
from .models import *

class NameForm(forms.Form):
    payee_name = forms.CharField(label='Payee name', max_length=100)


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageItem
        fields = ['image']
