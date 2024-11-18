from django import forms
from .models import Cat

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'breed', 'age', 'sexuality', 'color']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '🐾 Cat Name'}),
            'breed': forms.TextInput(attrs={'placeholder': '🐱 Cat Breed'}),
            'age': forms.NumberInput(attrs={'placeholder': '🎂 Age'}),
            'sexuality': forms.Select(attrs={'style': 'font-size: 16px;'}),
            'color': forms.Select(attrs={'style': 'font-size: 16px;'}),
        }
