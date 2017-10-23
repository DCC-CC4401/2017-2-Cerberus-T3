from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DenunciaForm, SignUpForm

from .models import Denuncia, UsuarioNormal, UsuarioMunicipalidad, UsuarioONG


def index(request):
    return render(request, 'index.html')


def denunciar(request):
    if request.method == 'POST':

        form = DenunciaForm(request.POST)

        if form.is_valid():
            d_abusos = form.cleaned_data['abuso']
            d_animal = form.cleaned_data['animal']
            d_sexo = form.cleaned_data['sexo']
            d_color = form.cleaned_data['color']
            d_herido = form.cleaned_data['herido']

            lugar_dummy = 'Avenida Almirante Beauchef 851, Santiago'
            denuncia = Denuncia(animal=d_animal, sexo=d_sexo, color=d_color, herido=d_herido, localizacion=lugar_dummy)
            denuncia.save()
            denuncia.abuso = d_abusos
            denuncia.save()

            messages.success(request, 'Denuncia realizada con éxito', extra_tags='alert')
            return redirect('index')

    else:
        form = DenunciaForm()

    return render(request, 'denunciar.html', {'form': form})


def crear_usuario(request):
    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():
            usuario = form.cleaned_data['username']
            clave1 = form.cleaned_data['password1']
            clave2 = form.cleaned_data['password2']
            tipo = form.cleaned_data['user_type']

            usar=''

            if tipo == 'Usuario':
                user = UsuarioNormal.objects.create_user(usuario)
            elif tipo == 'Municipalidad':
                user = UsuarioMunicipalidad.objects.create_user(usuario)
            else:
                user = UsuarioONG.objects.create_user(usuario)


            user.set_password(clave1)
            user.save()


            messages.success(request, 'Usuario ' + usuario + ' creado con éxito', extra_tags='alert')
            return redirect('index')

    else:
        form = SignUpForm()

    return render(request, 'signUp.html', {'form': form})
