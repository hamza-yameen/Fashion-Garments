from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class GuestForm(forms.Form):
    email = forms.EmailField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ReisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Conform Password", widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        om = User.objects.filter(username=username)
        if om.exists():
            raise forms.ValidationError("Username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        om = User.objects.filter(email=email)
        if om.exists():
            raise forms.ValidationError("Username is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        pass_1 = self.cleaned_data.get("password")
        pass_2 = self.cleaned_data.get("password2")
        if pass_1 != pass_2:
            raise forms.ValidationError("Password must be same.")
        return data
