# 애플리케이션 폴더의 urls.py

from django.urls import path
from .views import post_board_view, post_index_view
from .views import upvote_post_view, downvote_post_view, upload_comment
from .views import login_view

urlpatterns = [
    path('',post_board_view, name='post_board_view'),
    path('<int:post_id>/',post_index_view, name='post_index_view'),
    path('<int:post_id>/upvote/',upvote_post_view, name='upvote_post_view'),
    path('<int:post_id>/downvote/',downvote_post_view, name='downvote_post_view'),
    path('<int:post_id>/upload_comment/',upload_comment, name='upload_comment'),
    path('login/',login_view, name='login_view'),
]
