# NHS/NHSApp/views/__init__.py start
from .post_board import post_board_view
from .post_index import post_index_view, upvote_post_view, downvote_post_view, upload_comment_view
from .loginout import login_view, logout_view
from .account import account_view
__all__ = [
    'post_board_view',
    'post_index_view', 'upvote_post_view', 'downvote_post_view', 'upload_comment_view',
    'login_view', 'logout_view',
    'account_view'
]
# NHS/NHSApp/views/__init__.py end