from django.shortcuts import render

# Create your views here.
#One html web page for now
def chat_room(request):
    return render(request, 'network_app/chat_room.html')
