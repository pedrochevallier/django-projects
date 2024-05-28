import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import User, Game
from .coordinates import get_coordinates
from math import sqrt


class LobbyConsumer(WebsocketConsumer):
    def connect(self):
        self.roomName =  self.scope['url_route']['kwargs']['roomName']
        self.room_group_name = 'game_%s' % self.roomName
        
        game = Game.objects.get(gameName=self.roomName)
        print(game)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        print("connection accepted")
        game.connectedUsers = game.connectedUsers + 1
        game.save()
        if game.connectedUsers > 8:
            self.close()



    def disconnect(self, code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        game = Game.objects.get(gameName=self.roomName)
        game.connectedUsers = game.connectedUsers - 1
        game.save()

        User.objects.filter(channelsRoomName = self.channel_name).delete() 
        users = [i.json() for i in User.objects.filter(roomName = self.room_group_name[5:])]
        if users:
            users[0]['isKing'] = 1
        if not users:
            Game.objects.get(gameName=self.roomName).delete()
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'user_send',
                'action': 'user',
                'message': users
            }
        )


    # receive message from websocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # if action ==  user then send all data from users in room
        if text_data_json['action']=='new_user':
            userid = text_data_json['userID']
            userName = text_data_json['userName']
            userColor = text_data_json['userColor']
            isKing = text_data_json['isKing']
            #user = User.objects.get(uniqueUID = userid)
            channelsRoomName = str(self.channel_name)
            user = User(uniqueUID=userid, channelsRoomName=channelsRoomName,roomName=self.room_group_name[5:], userName=userName, userColor=userColor, isKing=isKing)
            user.save()
            users = [i.json() for i in User.objects.filter(roomName = user.roomName)]
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'user_send',
                    'action': 'user',
                    'message': users,
                }
            )
        # if action == startGame then send that game stated to all users in room
        if text_data_json['action']=='startGame':
            '''
            rounds = text_data_json['rounds']
            game = Game.objects.get(gameName=self.roomName)
            game.started = 1
            game.rounds = rounds
            game.save()
            '''
            coordinates = get_coordinates()

            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'start_game',
                    'action': 'starGame',
                    'coordinates':coordinates,
                }
            )
            game = Game.objects.get(gameName = self.roomName)
            game.started = 1
            game.save()

        if text_data_json['action']=='hasGameStarted':
            game = Game.objects.get(gameName = self.roomName)
            if game.started == 1:
                async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'game_started',
                    'action': 'gameStarted',
                }
            )

        if text_data_json['action']=='roundFinished':
            userCoordinates={
                'userID': text_data_json['userID'],
                'x': text_data_json['userx'],
                'y': text_data_json['usery'],
                'xcoordinate': text_data_json['x'],
                'ycoordinate': text_data_json['y'],
            }
            if userCoordinates['x']==None:
                score = 0
            else:
                score = 10000 * (1/sqrt(abs(userCoordinates['x'])**2 + abs(userCoordinates['y']**2)))
            user = User.objects.get(uniqueUID=text_data_json['userID'])
            user.userScore = user.userScore + int(score)
            user.save()
            users = [i.json() for i in User.objects.filter(roomName = user.roomName)]
            
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'round_finished',
                    'action': 'userScores',
                    'message': users,
                    'coordinates': userCoordinates,
                }
            )
            
    
    # Send all user data
    def user_send(self, event):
        action = event['action']
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'action': action,
            'message': message,
        }))

    
    # Send all users that game started
    def start_game(self, event):
        action = event['action']
        message = event['coordinates']
        
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'action': action,
            'message': message,
        }))


    def game_started(self, event):
        action = event['action']

        self.send(text_data=json.dumps({
            'action': action,
        }))

    def round_finished(self, event):
        action = event['action']
        message = event['message']
        coordinates = event['coordinates']

        self.send(text_data=json.dumps({
            'action': action,
            'message': message,
            'coordinates': coordinates,
        }))