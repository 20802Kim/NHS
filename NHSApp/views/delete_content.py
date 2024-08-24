# NHS/NHSApp/views/delete_content.py start
from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Post, Comment

def delete_post_view(request, post_id):
    post=Post.objects.get(pk=post_id)
    if post.author == request.user or request.user.is_superuser:
        post.delete()
        return redirect('post_board_view')
    else:
        messages.error(request, '권한이 없습니다!')
        return redirect('post_index_view', post_id)

def delete_comment_view(request, post_id, comment_id):
    comment=Comment.objects.get(pk=comment_id)
    if comment.author == request.user or request.user.is_superuser:
        comment.delete()
    else:
        messages.error(request, '권한이 없습니다!')
    return redirect('post_index_view', post_id)

# NHS/NHSApp/views/delete_content.py end