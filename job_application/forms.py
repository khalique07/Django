from django import forms

class ContactForm(forms.Form):
    """
    Form for job application input
    Mirrors the Model structure but for frontend
    """
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)