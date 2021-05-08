from django import forms

class CustomForm(forms.Form):
    content = forms.CharField(max_length=50, required=True)