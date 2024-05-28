from django.shortcuts import render
from .models import User, Game
from .idGenerator import user_id_generator, room_id_generator
from .color import random_color


def index(request):
    userID = user_id_generator()
    roomName = room_id_generator()
    color = random_color()
    game = Game(gameName=roomName)
    game.save()
    return render(request, 'game/index.html',{'roomName': roomName, 'userid': userID, 'userColor':color, 'isKing':1})
    

def index2(request, roomName):
    userID = user_id_generator()
    color = random_color()
    return render(request, 'game/index.html',{'roomName': roomName, 'userid': userID, 'userColor': color, 'isKing':0})

