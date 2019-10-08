from django import forms

class WordForm(forms.Form):
    post = forms.CharField(label='Please type your word here', max_length=100, required = True)
