# NHS/NHSApp/views/post_board.py start
from django.shortcuts import render
from ..models import Post

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
# NHS/NHSApp/views/post_board.py end