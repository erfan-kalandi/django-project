from django import forms
from .models import *


class poemform(forms.ModelForm):
    class Meta:
        model = poem
        fields = ('poet','title', 'text' )


