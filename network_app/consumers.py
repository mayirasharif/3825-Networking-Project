import json
from channels.generic.websocket import WebsocketConsumer #Needed for socket library
from asgiref.sync import async_to_sync #Need it for multiple clients
import uuid
#This class essentially represents all of the code for the server to help it handle responses and connections.

class Consumer(WebsocketConsumer):
    #This function is used to connect a client to the server
    def connect(self):
        self.room_group_name = 'test'
        self.unique_id = uuid.uuid4()

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        # Trying to tell client which other clients are connected to server
        message = str(self.unique_id)
        message = 'Client: '+ message+ ' connected!'
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message': message
            }
        )
        print('New Connection', self.unique_id)
        self.accept()

    #This function is used for the server to receive info from the client   
    def receive(self, text_data):
        text = json.loads(text_data)
        message = text['message']
        unique_id = str(self.unique_id)
        #message = unique_id + ': ' + message
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
        unique_id = str(self.unique_id)
        #message = unique_id + ': ' + message
        self.send(text_data = json.dumps({
            'type':'chat',
            'message':message
        }))
    
    #This is how the clients can disconnect from the server
    def disconnect(self, close_code):
        print('Socket is disconnected!', close_code)

    