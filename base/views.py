from django.shortcuts import render

# Create your views here.

rooms = [
{

  'id':1, 'name': 'Lets learn Python!'
},
{
  'id':2, 'name': 'Design with me!'
},
{
  'id':3, 'name': 'Frontend Developer!'
},
{
  'id':4, 'name': 'Backend Developer!'
},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for item in rooms:
        if item['id'] == int(pk):
            room = item

    context = {'room': room}

    return render(request, 'base/room.html',context)
