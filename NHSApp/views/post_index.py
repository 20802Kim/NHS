# NHS/NHSApp/views/post_index.py start

# post_index (글 상세 정보) 함수 선언

from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Post, Comment

def post_index_view(request, post_id):
    post=Post.objects.get(pk=post_id)
    post_list=list(Post.objects.order_by('-pub_date'))
    post.views+=1
    post.save()
    comment_list=list(Comment.objects.filter(post=post).order_by('pub_date'))
    n_post_list=Post.objects.filter(category='공지').order_by('-pub_date')
    context={
        'user':request.user,
        'post':post,
        'comment_list':comment_list,
        'post_list':post_list,
        'n_post_list':n_post_list
    }
    return render(request, 'NHSApp/post_index.html', context)

def upvote_post_view(request, post_id):
    post=Post.objects.get(pk=post_id)
    if post.add_upvote(request.user):
        return redirect('post_index_view', post_id)
    else:
        messages.error(request, '이미 추천했습니다!')
        return redirect('post_index_view', post_id)
def downvote_post_view(request, post_id):
    post=Post.objects.get(pk=post_id)
    if post.add_downvote(request.user):
        return redirect('post_index_view', post_id)
    else:
        messages.error(request, '이미 비추천했습니다!')
        return redirect('post_index_view', post_id)
# NHS/NHSApp/views/post_index.py end