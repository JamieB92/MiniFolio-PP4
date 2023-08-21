from django.contrib import admin
from .models import userPosts
from .models import postComments
from django_summernote.admin import SummernoteModelAdmin


@admin.register(userPosts)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('header', 'posted_on', 'creator',)
    search_fields = ['header', 'creator',]
    list_filter = ('posted_on',)
    summernote_fields = ('caption')


@admin.register(postComments)
class CommentsAdmin(admin.ModelAdmin):

    list_display = ('name', 'created_on', 'comment_body',)
    list_filter = ('created_on',)
