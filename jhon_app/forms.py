from .models import MovieVerse
from django import forms

class MovieVerseForm(forms.ModelForm):
    class Meta:
        model = MovieVerse
        fields = ['title_name', 'type', 'genre', 'status', 'rating']

        widgets = {
            'title_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title name'}),
            'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter type'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter genre'}),
            'status': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter status'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter rating'}),
        }