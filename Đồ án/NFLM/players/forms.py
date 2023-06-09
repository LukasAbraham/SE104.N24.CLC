from django import forms
from django.forms import ModelForm
from login.models import Player

# Create a Player form

class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = "__all__"