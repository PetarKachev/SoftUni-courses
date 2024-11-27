from django import forms
from .models import Event
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'category']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class EventModifyForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'category']


class EventDeleteForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['readonly'] = 'readonly'
        self.fields['description'].widget.attrs['readonly'] = 'readonly'
        self.fields['location'].widget.attrs['readonly'] = 'readonly'
        self.fields['date'].widget.attrs['readonly'] = 'readonly'
        self.fields['category'].widget.attrs['disabled'] = 'disabled'


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

