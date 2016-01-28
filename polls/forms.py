from django import forms
from .models import SignUp

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 150)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ["name", "email"]
       # exclude = ["email"]   HIGHLY RECOMMENDED THAT, EXCLUDE shouldn't use
    def clean_email(self):
        email= self.cleaned_data.get("email")
        email_base, provider = email.split("@")
        domain, extension = provider.split(".")
        if not "com" in email:
            raise forms.ValidationError("Please enter a valid COM email")
        return email


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )