from django import forms
from .models import Habit
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils import timezone


class HabitForm(ModelForm):
    class Meta:
        start_date = forms.DateTimeField(
            widget=forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}))

        model = Habit
        fields = ['name', 'description', 'end_date', 'required_count']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Description'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'required_count': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        if end_date < timezone.now().date():
            raise ValidationError("The end date cannot be in the past.")
        return end_date


class HabitUpdateCountForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['current_count']
        widgets = {
            'current_count': forms.NumberInput(attrs={'min': '0'}),
        }
