from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)

from api.permissions import AuthorOrReadOnly
from api.serializers import (GroupSerializer, PostSerializer,
                             CommentSerializer, FollowSerializer)
from api.viewsets import CreateAndListViewSet
from posts.models import Group, Post, Follow, User


class PostViewSet(viewsets.ModelViewSet):
    """Список постов."""
    queryset = Post.objects.select_related('author')
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,
                          IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Список групп."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    """Список комментариев."""
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,
                          IsAuthenticatedOrReadOnly)

    def get_post(self):
        """
        Функция возвращает post чтобы не дублировать код
        его получения в get_queryset() и perform_create().
        """
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post

    def get_queryset(self):
        post = self.get_post()
        queryset = post.comments.select_related('author')
        return queryset

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(CreateAndListViewSet):
    """Список подписок."""
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """
        Для получения queryset используем prefetch_related,
        т.к. user и following имеют отношение "многие-ко-многим".
        Экспериментальным путём установлено, что
        длина запроса уменьшается в разы.
        """
        user = get_object_or_404(User, username=self.request.user)
        queryset = Follow.objects.prefetch_related(
            'user', 'following').filter(user=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
