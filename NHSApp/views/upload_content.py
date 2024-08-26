# NHS/NHSApp/views/upload_content.py start

# 콘텐츠 업로드 관련 함수 선언

from django.shortcuts import render, redirect
from ..models import Post, Comment

def upload_post_view(request):
    context={}
    if request.method == 'POST':
        category_ko=list(tab_ko for (tab_ko, tab_en) in Post.CATEGORY_CHOICES)
        category_en=list(tab_en for (tab_ko, tab_en) in Post.CATEGORY_CHOICES)
        title=request.POST.get('title')
        content=request.POST.get('content').replace('\r\n','\n')
        category=request.POST.get('category')
        if category in category_en:category=category_ko[category_en.index(category)]
        post=Post.objects.create(author=request.user, title=title, content=content, category=category)
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