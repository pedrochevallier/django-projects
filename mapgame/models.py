from django.db import models
from sqlalchemy import null

class User(models.Model):
    userName = models.CharField(max_length=20)
    uniqueUID = models.CharField(max_length=20)
    roomName = models.CharField(max_length=20)
    userScore = models.IntegerField(default=0)
    channelsRoomName = models.CharField(max_length=100)
    userColor = models.CharField(max_length=7)
    isKing = models.IntegerField(default=0)

    def json(self):
        return {
            'userName': self.userName,
            'uniqueUID': self.uniqueUID,
            'roomName': self.roomName,
            'userScore': self.userScore,
            'channelsRoomName': self.channelsRoomName,
            'userColor': self.userColor,
            'isKing':self.isKing,
        }

class Game(models.Model):
    gameName = models.CharField(max_length=20, default=null)
    rounds = models.IntegerField(default=0)
    round = models.IntegerField(default=0)
    connectedUsers = models.IntegerField(default=0)
    started = models.IntegerField(default=0)