from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import userPosts
from .models import postComments


class LandingPage(View):
    def get(self, request):
        return render(request, "index.html")


class UploadList(generic.ListView):
    def get(self, request):
        comments = postComments.objects.all()
        posts = userPosts.objects.all()
        context = {
            'comments': comments,
            'posts': posts
        }
        return render(request, 'home.html', context)
