from django import forms
from .models import hashcatmode

class UnhashForm(forms.Form): 
    hash_text = forms.CharField(
        label='Hash Text',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    hash_type = forms.ModelChoiceField(
        label='Hash Type',
        queryset=hashcatmode.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )