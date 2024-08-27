# NHS/NHSApp/views/page.py start
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

def post_board_view(request):
    context={}
    search_query = request.GET.get('search', '')
    tab=request.GET.get('tab', '전체')

    post_list=Post.objects.all().order_by('-pub_date')
    if tab!='전체':post_list=post_list.filter(category=tab)
    if search_query:post_list=post_list.filter(title__icontains=search_query)

    n_post_list=Post.objects.filter(category='공지').order_by('-pub_date')
    categories = ['전체']+list(Post.objects.values_list('category', flat=True).distinct())
    if '공지' in categories:
        categories.remove('공지')
    context['user']=request.user
    context['post_list']=post_list
    context['categories']=categories
    context['current_tab']=tab
    context['n_post_list']=n_post_list
    
    return render(request, 'NHSApp/post_board.html', context)
# NHS/NHSApp/views/page.py end