from django.shortcuts import render
from .models import Ranking, Tanque, Win8


def home(request):
    paso_ranking = Ranking.objects.all()
    paso_win8 = Win8.objects.all()
    paso_tanques = Tanque.objects.all()
    return render(request, "home.html", {"paso_ranking": paso_ranking, "paso_win8": paso_win8, "paso_tanques": paso_tanques})


def ranking(request):
    paso_ranking = Ranking.objects.all()
    return render(request, "widget_ranking.html", {"paso_ranking": paso_ranking})


def win8(request):
    paso_win8 = Win8.objects.all()
    return render(request, "widget_win8.html", {"paso_win8": paso_win8})


def tanques(request):
    paso_tanques = Tanque.objects.all()
    return render(request, "widget_tanques.html", {"paso_tanques": paso_tanques})
