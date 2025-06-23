from django import forms
from django.contrib.auth.models import User
from .models import Contact, Category

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'address', 'category']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Remove 'user' from kwargs
        super().__init__(*args, **kwargs)
        if user:
            # Filter categories by this user
            self.fields['category'].queryset = Category.objects.filter(user=user)
        else:
            self.fields['category'].queryset = Category.objects.none()


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
