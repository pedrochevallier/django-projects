# views.py
from django.shortcuts import render

def cards_view(request):
    cards = [
        {'title': 'QR Code Generator', 'link': '/qr'},
        {'title': 'URL Shortener', 'link': '/url'},
        {'title': 'Map Game', 'link': '/game'}
    ]
    context = {'cards': cards}
    return render(request, 'cards_template.html', context)

