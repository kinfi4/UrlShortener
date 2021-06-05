from django import forms


class TranslateUrlForm(forms.Form):
    short_url = forms.CharField(max_length=7, required=True, label='Enter shortened url: ')


class CutUrlForm(forms.Form):
    full_url = forms.CharField(max_length=200, required=True, label='Enter the url you want to be cut: ')
