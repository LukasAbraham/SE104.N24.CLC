from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    username = request.user.username
    context = {
        'username': username
    }
    return render(request, 'pages/teams.html',context)

def logout_user(request):
    logout(request)
    return redirect('/login')