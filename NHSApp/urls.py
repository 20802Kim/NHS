# NHS/NHSApp/urls.py start
# views랑 url을 연결

from django.urls import path
from .views import post_board_view, post_index_view
from .views import upvote_post_view, downvote_post_view
from .views import upload_comment_view, upload_post_view
from .views import login_view, logout_view, account_view
from .views import delete_post_view, delete_comment_view

urlpatterns = [
    path('',post_board_view, name='post_board_view'),
    path('upload_post/',upload_post_view, name='upload_post_view'),
    path('<int:post_id>/',post_index_view, name='post_index_view'),
    path('<int:post_id>/upvote/',upvote_post_view, name='upvote_post_view'),
    path('<int:post_id>/downvote/',downvote_post_view, name='downvote_post_view'),
    path('<int:post_id>/upload_comment/',upload_comment_view, name='upload_comment_view'),
    path('<int:post_id>/delete_post/',delete_post_view, name='delete_post_view'),
    path('<int:post_id>/delete_comment/<int:comment_id>',delete_comment_view, name='delete_comment_view'),
    path('login/',login_view, name='login_view'),
    path('logout/',logout_view, name='logout_view'),
    path('account/<str:username>',account_view, name='account_view'),
]

# NHS/NHSApp/urls.py end