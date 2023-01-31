from .models import Room
from django import forms


class NewRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'slug']


class DeleteRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']
