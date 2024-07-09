from django import forms
from users.models import User


class HabitForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()
    current_streak = forms.IntegerField()
    is_completed = forms.BooleanField()

    user = forms.ModelChoiceField(queryset=User.objects.all())
