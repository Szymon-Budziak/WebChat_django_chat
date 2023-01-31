from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import SignUpForm


def frontpage(request):
    users = get_logged_in_users()
    return render(request, 'core/frontpage.html', {'users': users})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


def get_logged_in_users():
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []
    for session in sessions:
        data = session.get_decoded()
        uid = data.get('_auth_user_id', None)
        if uid:
            uid_list.append(uid)
    return User.objects.filter(id__in=uid_list)
