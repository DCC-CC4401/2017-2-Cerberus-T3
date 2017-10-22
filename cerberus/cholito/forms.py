from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import ModelForm
from .models import Denuncia
from django.utils.translation import ugettext_lazy as _


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


class DenunciaForm(ModelForm):
    class Meta:
        model = Denuncia
        fields = ['abuso', 'animal', 'sexo', 'color', 'herido']
        labels = {
            'abuso': _('Abuso'),
            'animal': _('Animal'),
            'sexo': _('Sexo'),
            'color': _('Color'),
            'herido': _('Herido'),
        }
        widgets = {
            'sexo': forms.RadioSelect,
            'abuso': forms.CheckboxSelectMultiple,
            'herido': forms.NullBooleanSelect,
        }
