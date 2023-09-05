from django.shortcuts import render
from django.views.generic.list import ListView
from .models import userPosts
from .models import userProfiles


class UserProfile(ListView):
    model = userPosts
    model = userProfiles
    template_name = "profile.html"

