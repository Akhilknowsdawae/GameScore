from django.shortcuts import render, redirect

from .models import Game, Review, UserReview


def mainPage(request):
    game = Game.objects.get(id=1)
    context = {
        'game': game,
    }
    return render(request, 'homePage.html', context)


def gamePage(request):
    game = Game.objects.get(id=1)
    reviews = Review.objects.filter(gameID_id=game.id)
    context = {
        'game': game,
        'reviews': reviews,
    }

    return render(request, 'gamePage.html', context)


def gameReviewView(request):
    game = Game.objects.get(id=1)
    reviews = Review.objects.filter(gameID_id=game.id)
    context = {
        'game': game,
        'reviews': reviews,
    }

    return render(request, 'gameReviewPage.html', context)


def submitReview(request):
    userInput = request.POST

    print(userInput)

    newReview = Review()

    newReview.title = userInput.get('Title')
    newReview.description = userInput.get('Description')
    newReview.score = 5
    newReview.gameID = Game.objects.get(id=1)
    newReview.userID = UserReview.objects.get(id=1)

    newReview.save()

    return redirect('index')
