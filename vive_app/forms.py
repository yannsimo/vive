from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'prenom', 'email', 'type_contact', 'message']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Votre nom',
                'autocomplete': 'name',
            }),
            'prenom': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Votre prénom',
                'autocomplete': 'given-name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'exemple@email.com',
                'autocomplete': 'email',
            }),
            'type_contact': forms.Select(attrs={
                'class': 'form-input',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 4,
                'placeholder': 'Partagez-nous votre projet ou vos questions...',
            }),
        }