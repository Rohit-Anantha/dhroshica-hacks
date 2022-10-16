from django import forms
from .models import *

class NameForm(forms.Form):
    payer_name = forms.CharField(label='Add new payer', max_length=100)



class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageItem
        fields = ['image']
