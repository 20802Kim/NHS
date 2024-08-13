from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import time
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_board_view')
        else:
            context={
                'error':'Invalid username or password'
            }
            return render(request, 'NHSApp/login.html', context)
    return render(request, 'NHSApp/login.html')