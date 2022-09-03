from django import forms


class OderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form_control'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form_control'}))
