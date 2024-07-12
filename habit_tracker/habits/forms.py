from django import forms
from .models import Habit
from django.forms import ModelForm


class HabitForm(ModelForm):
    class Meta:
        start_date = forms.DateTimeField(
            widget=forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))

        model = Habit
        fields = ['name', 'description', 'end_date', 'current_streak', 'is_completed', 'user']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'current_streak': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }

