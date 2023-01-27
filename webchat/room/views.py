from django.shortcuts import render
from .models import Room, Message
from .forms import NewRoomForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect


@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[:25]
    return render(request, 'room/room.html', {'room': room, 'messages': messages})


@staff_member_required
def new_room(request):
    if request.method == "POST":
        form = NewRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms')
    else:
        form = NewRoomForm()
    return render(request, 'room/new_room.html', {'form': form})
