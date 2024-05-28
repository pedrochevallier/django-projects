# views.py
from django.shortcuts import render

def cards_view(request):
    cards = [
        {'title': 'Card 1', 'link': '/qr', 'description': 'This is the first card.'},
        {'title': 'Card 2', 'link': '/url', 'description': 'This is the second card.'},
        {'title': 'Card 3', 'link': '/game', 'description': 'This is the third card.'}
    ]
    context = {'cards': cards}
    return render(request, 'cards_template.html', context)

