import json
from channels.generic.websocket import WebsocketConsumer #Needed for socket library
from asgiref.sync import async_to_sync #Need it for multiple clients

#This class essentially represents all of the code for the server to help it handle responses and connections.

class Consumer(WebsocketConsumer):
    #This function is used to connect a client to the server
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    #This function is used for the server to receive info from the client   
    def receive(self, text_data):
        text = json.loads(text_data)
        message = text['message']
        print(message)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message': message
            }
        )

    #This is how one client can send a message to another client using the server.
    def chat_message(self,event):
        message = event['message']
        self.send(text_data = json.dumps({
            'type':'chat',
            'message':message
        }))
    
    #This is how the clients can disconnect from the server
    #def disconnect(self, close_code)