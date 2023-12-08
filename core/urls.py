from django.urls import path
from core.views import HomeView, PostCreateView, PostLikeUnlikeView, PostCommentView, CommentsView, FollowUnfollowView
from django.contrib.auth.decorators import  login_required      # login decorator
# We want our home_feed to be accessible only when user is logged in

urlpatterns = [
    path('feed/', login_required(HomeView.as_view()) , name='home_feed_view'),
    
    path('post/create/', login_required(PostCreateView.as_view()), name='post_create_view'),

    path('post/like-unlike/<int:id>/', PostLikeUnlikeView.as_view(), name='post_like_unlike_view'),
    path('post/comment/<int:id>/', PostCommentView.as_view(), name='post_comment_view'),
    path('post/comments/<int:id>/', CommentsView.as_view(), name='comment_page'),
    path('in/<str:username>/followUnfollow/', login_required(FollowUnfollowView.as_view()), name='follow_unfollow_view'), 
]