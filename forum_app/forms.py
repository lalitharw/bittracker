from django import forms
from .models import *

class ForumAddLogForm(forms.ModelForm):
    class Meta:
        model = ForumAddLog
        fields = ['track_unit']

class ForumForm(forms.ModelForm):
    class Meta:
        model = ForumGroups
        fields = '__all__'