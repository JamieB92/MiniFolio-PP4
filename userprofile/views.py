from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import userPosts
from .models import userProfiles


class UserProfile(ListView):
    model = userProfiles
    template_name = "profile.html"

    # def get_profile(self):
    #     return self.request.user


class CreateUserProfile(CreateView):
    model = userProfiles
    fields = ['profile_image', 'profile_bio']
    template_name = "create-profile.html"
    success_url = "/home"