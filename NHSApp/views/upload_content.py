# NHS/NHSApp/views/upload_content.py start
from django.shortcuts import render, redirect
from ..models import Post, Comment

def upload_post_view(request):
    context={}
    if request.method == 'POST':
        title=request.POST.get('title')
        content=request.POST.get('content').replace('\r\n','\n')
        post=Post.objects.create(author=request.user, title=title, content=content)
        return redirect('post_index_view', post.pk)
    else:
        context['user']=request.user
        return render(request, 'NHSApp/write_post.html', context)

def upload_comment_view(request, post_id):
    post=Post.objects.get(pk=post_id)
    content=request.POST.get('content').replace('\r\n','\n')
    Comment.objects.create(post=post, author=request.user, content=content)
    return redirect('post_index_view', post_id)
# NHS/NHSApp/views/upload_content.py end