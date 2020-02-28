from django import forms
from .models import Recurt, Sith, ShadowHand

class RecurtForm(forms.ModelForm):
    class Meta:
        model = Recurt
        fields = ('name', 'planet', 'age', 'email','question1', 'question2', 'question3',)

class SithForm(forms.ModelForm):
    class Meta:
        model = Sith
        fields = ('sith_name', 'planet_learn',)

class ShadowHandForm(forms.ModelForm):
    class Meta:
        model = ShadowHand
        fields = ('name', 'email',)