from django.shortcuts import render
from django.http import HttpResponse
from .models import Game

# Create your views here.


def home(request):
    context = {
        'games': Game.objects.all()
    }
    return render(request, 'blindchess/home.html', context)


def game(request):
    return render(request, 'blindchess/game.html')
