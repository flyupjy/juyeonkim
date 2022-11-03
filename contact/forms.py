from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    sender = forms.CharField(
        max_length = 128,
        widget=forms.TextInput(attrs={
            'class': 'uk-input',
            'placeholder': 'example@example.com',
        })
    )
    subject = forms.CharField(
        max_length = 128,
        widget=forms.TextInput(attrs={
            'class': 'uk-input',
            'placeholder': 'example subject',
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'uk-textarea',
            'rows': 8,
        })
    )
    
    class Meta:
        model = Contact
        fields = ('sender', 'subject', 'message')
