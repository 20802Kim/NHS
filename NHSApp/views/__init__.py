# NHS/NHSApp/views/__init__.py start
from .upload_content import upload_comment_view, upload_post_view, upvote_post_view, downvote_post_view
from .account import account_view, login_view, logout_view
from .delete_content import delete_post_view, delete_comment_view
from. page import post_board_view, post_index_view
__all__ = [
    'post_board_view',
    'post_index_view', 'upvote_post_view', 'downvote_post_view',
    'upload_comment_view', 'upload_post_view',
    'account_view', 'login_view', 'logout_view',
    'delete_post_view', 'delete_comment_view',
]
# NHS/NHSApp/views/__init__.py end