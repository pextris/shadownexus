from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Custom registration form using email instead of username
class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    handle = forms.CharField(
        max_length=20,
        required=False,
        help_text="Enter your in-game alias"
    )

    class Meta:
        model = User
        fields = ['email', 'handle', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Use email as username
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# Custom login form using email
class EmailLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("Invalid email or password.")

            self.user = authenticate(username=user.username, password=password)
            if self.user is None:
                raise forms.ValidationError("Invalid email or password.")
        return self.cleaned_data

    def get_user(self):
        return self.user
