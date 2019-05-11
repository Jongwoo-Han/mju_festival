from django import forms
from .models import Lost

class LostForm(forms.ModelForm):
    class Meta:
        model = Lost
        fields = ['title', 'author', 'image', 'content', 'password']