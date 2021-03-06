from django.shortcuts import render

from .models import Room

# Create your views here.

# rooms = [
# {

#   'id':1, 'name': 'Lets learn Python!'
# },
# {
#   'id':2, 'name': 'Design with me!'
# },
# {
#   'id':3, 'name': 'Frontend Developer!'
# },
# {
#   'id':4, 'name': 'Backend Developer!'
# },
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    # for item in rooms:
    #     if item['id'] == int(pk):
    #         room = item

    context = {'room': room}

    return render(request, 'base/room.html',context)

def createRoom(request):
  context = {}
  return render(request, 'base/room_form.html', context)
