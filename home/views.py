from django.shortcuts import render
from django.views import generic
from .models import userPosts


class UploadList(generic.ListView):
    model = userPosts
    queryset = userPosts.objects.order_by("-posted_on")
    template_name = "index.html"
