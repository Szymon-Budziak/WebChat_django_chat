from django.shortcuts import render
from .models import Room, Message
from .forms import NewRoomForm, DeleteRoomForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist


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


@staff_member_required
def delete_room(request):
    if request.method == 'POST':
        form = DeleteRoomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            try:
                room = Room.objects.get(name=name)
                room.delete()
            except ObjectDoesNotExist:
                return redirect('delete_room')
            return redirect('rooms')
    else:
        form = DeleteRoomForm()
    return render(request, 'room/delete_room.html', {'form': form})
