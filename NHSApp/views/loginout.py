# NHS/NHSApp/views/login.py start
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    context={}
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('loggedin succesfully')
            return redirect('post_board_view')
        else:
            context['error']='Invalid username or password'
            print('login failed')
            return render(request, 'NHSApp/login.html', context)
    return render(request, 'NHSApp/login.html')
def logout_view(request):
    logout(request)
    return redirect('post_board_view')
# NHS/NHSApp/views/login.py end