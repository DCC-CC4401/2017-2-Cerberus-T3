from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuario", max_length=40,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Usuario', 'name': 'Usuario'}))

    password = forms.CharField(label="Contraseña", max_length=40,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Contraseña', 'name': 'Contraseña'}))

    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        if not self.cleaned_data.get('remember_me'):
            self.request.session.set_expiry(0)

        return cleaned_data
