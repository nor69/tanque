from django.shortcuts import render
from .models import Repeticione
from .forms import RepeticionesForm


def repeticiones(request):
    a = 'nivel'
    b = 'nivel'
    c = 'nivel'
    if request.method == 'POST':
        form_repeticiones = RepeticionesForm(request.POST)
        if form_repeticiones.is_valid():
            a = form_repeticiones.cleaned_data['lista_uno']
            b = form_repeticiones.cleaned_data['lista_dos']
            c = form_repeticiones.cleaned_data['lista_tres']

    else:
        form_repeticiones = RepeticionesForm()
        a = 'nivel'
        b = 'nivel'
        c = 'nivel'

    Repeticione.objects.all()

    repeticiones = Repeticione.objects.all().order_by(a, b, c)

    return render(request, "repeticiones.html", {"repeticiones": repeticiones, 'form_repeticiones': form_repeticiones})


def video(request, paso_id):
    paso_video = Repeticione.objects.get(id=paso_id)
    return render(request, "video.html", {"paso_video": paso_video})
