# NHS/NHSApp/views/account.py start
from django.shortcuts import render
from ..models import Post
from django.contrib.auth.models import User
import time

def account_view(request, username):
    account=User.objects.get(username=username)
    post_list=list(Post.objects.filter(author=account).order_by('-pub_date'))
    context={
        'now':time.localtime(time.time()),
        'user':request.user,
        'account':account,
        'post_list':post_list
    }
    return render(request, 'NHSApp/account.html', context)
# NHS/NHSApp/views/account.py end