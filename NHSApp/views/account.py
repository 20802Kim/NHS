# NHS/NHSApp/views/account.py start

# 계정 관련 함수 선언

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from ..models import Post
from django.contrib.auth.models import User

def account_view(request, username):
    account=User.objects.get(username=username)
    post_list=list(Post.objects.filter(author=account).order_by('-pub_date'))
    context={
        'user':request.user,
        'account':account,
        'post_list':post_list
    }
    return render(request, 'NHSApp/account.html', context)
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
# NHS/NHSApp/views/account.py end