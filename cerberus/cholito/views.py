from django.shortcuts import render, redirect
from django.contrib import messages
from cholito.forms import DenunciaForm

from cholito.models import Denuncia


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
            print('NO ES VALIDO M3N')

    else:
        form = DenunciaForm()

    return render(request, 'denunciar.html', {'form': form})
