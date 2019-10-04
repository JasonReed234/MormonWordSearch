from django import forms

class WordForm(forms.Form):
    your_word = forms.CharField(label='Type your word here', max_length=100, required = True)

    