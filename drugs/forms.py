from django import forms
from .models import Drug


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ['name']
