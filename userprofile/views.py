from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import userPosts
from .models import userProfiles


class UserProfile(ListView):
    model = userPosts
    model = userProfiles
    template_name = "profile.html"


class CreateUserProfile(CreateView):
   fields = ['Profile_image', 'profile_bio']