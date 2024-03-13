from django.shortcuts import render

from .models import Game, Review


def mainPage(request):
    return render(request, 'index.html')


def gamePage(request):
    return render(request, 'GamePage.html')


def gameReviewView(request):
    game = Game.objects.get(id=1)
    reviews = Review.objects.filter(gameID_id=game.id)
    context = {
        'game': game,
        'reviews': reviews,
    }

    return render(request, 'gameReviewPage.html', context)
