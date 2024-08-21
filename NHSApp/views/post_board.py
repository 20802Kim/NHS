from django.shortcuts import render
from ..models import Post

def post_board_view(request):
    post_list=list(Post.objects.order_by('-pub_date'))
    context={
        'user':request.user,
        'post_list':post_list
    }
    return render(request, 'NHSApp/post_board.html', context)