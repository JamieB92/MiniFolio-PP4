from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import userPosts
from .models import postComments
from .forms import CommentForm


class LandingPage(View):
    def get(self, request):
        return render(request, "index.html")


class UploadList(generic.ListView):
    def get(self, request):
        posts = userPosts.objects.order_by("-posted_on")
        comments = postComments.objects.order_by("-created_on")
        return render(
            request, "home.html",
            {
                "posts": posts,
                "comments": comments,
                "comment_form": CommentForm()
            }
        )
