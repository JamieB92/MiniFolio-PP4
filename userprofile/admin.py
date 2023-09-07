from django.contrib import admin
from .models import userProfiles
from django_summernote.admin import SummernoteModelAdmin


@admin.register(userProfiles)
class ProfileAdmin(SummernoteModelAdmin):

    list_display = ('user', 'profile_image', 'profile_bio')
    search_fields = ['user']
    summernote_fields = ('profile_bio')
