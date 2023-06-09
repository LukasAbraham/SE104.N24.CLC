from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import PlayerForm
# Create your views here.
def index(request):
    username = request.user.username
    context = {
        'username': username
    }
    return render(request, 'pages/players.html',context)

def logout_user(request):
    logout(request)
    return redirect('/login')

def add_player(request):
    submitted = False
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_player?submitted=True')
    else:
        form = PlayerForm
        if 'submitted' in request.GET:
            submitted = True
    username = request.user.username
    context = {
        'username': username,
        'form': form,
        'submitted': submitted
    }
    return render(request, 'pages/add_player.html',context)
