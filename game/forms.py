from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import CustomUser, FACTION_CHOICES

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    handle = forms.CharField(
        max_length=20,
        required=False,
        help_text="Enter your in-game alias"
    )
    faction = forms.CharField(
        max_length=1,
        required=True,
        help_text="Enter a number corresponding to your faction"
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'handle', 'faction', 'password1', 'password2']

    def clean_faction(self):
        faction_input = self.cleaned_data['faction']
        try:
            index = int(faction_input) - 1
            if index < 0 or index >= len(FACTION_CHOICES):
                raise ValueError
        except (ValueError, TypeError):
            raise forms.ValidationError("Invalid faction number selected.")
        return FACTION_CHOICES[index][0]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.handle = self.cleaned_data['handle']
        user.faction = self.cleaned_data['faction']
        if commit:
            user.save()
        return user

class EmailLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            self.user = authenticate(email=email, password=password)
            if self.user is None:
                raise forms.ValidationError("Invalid login credentials")
        return cleaned_data

    def get_user(self):
        return self.user
