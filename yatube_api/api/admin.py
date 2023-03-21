from django.contrib import admin

from posts.models import Group, Post, Comment, Follow


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    list_editable = ('group',)
    search_fields = ('text', 'title',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
    list_per_page = 15


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description',)
    search_fields = ('text',)
    list_filter = ('title',)
    empty_value_display = '-пусто-'
    list_per_page = 15


@admin.register(Comment)
class GroupComment(admin.ModelAdmin):
    list_display = ('pk', 'post', 'author', 'text', 'created',)
    list_editable = ('text', 'author',)
    search_fields = ('text', 'author__username',)
    list_filter = ('created',)
    list_per_page = 15
    empty_value_display = '-пусто-'


@admin.register(Follow)
class GroupFollow(admin.ModelAdmin):
    list_display = ('user', 'following',)
    search_fields = ('user__username', 'following__username',)
    list_per_page = 30
