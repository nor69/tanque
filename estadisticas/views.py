from django.shortcuts import render
from .models import Estadistica
from .forms import EstadisticasForm


def estadisticas(request):
    a = 'nivel'
    b = 'nivel'
    c = 'nivel'
    if request.method == 'POST':
        form_estadisticas = EstadisticasForm(request.POST)
        if form_estadisticas.is_valid():
            a = form_estadisticas.cleaned_data['lista_uno']
            b = form_estadisticas.cleaned_data['lista_dos']
            c = form_estadisticas.cleaned_data['lista_tres']

    else:
        form_estadisticas = EstadisticasForm()
        a = 'nivel'
        b = 'nivel'
        c = 'nivel'

    Estadistica.objects.all()

    estadisticas = Estadistica.objects.all().order_by(a, b, c)

    for item in estadisticas:
        item.subtotal = (
            (item.experiencia+(50-item.victorias)+(item.batallas/10))*1.25)/100
        item.subtotal = round(item.subtotal, 2)
        item.save()
    for item in estadisticas:
        item.total = (item.subtotal+item.win8/100)/2
        item.total = round(item.total, 3)
        item.save()

    return render(request, "estadisticas.html", {"estadisticas": estadisticas, 'form_estadisticas': form_estadisticas})
