from django.urls import path, include
from rest_framework import routers

from .views import (CommentViewSet, PostViewSet,
                    GroupViewSet, FollowViewSet)

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
router.register(r'follow', FollowViewSet, basename='followers')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
