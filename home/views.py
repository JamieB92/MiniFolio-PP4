from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import userPosts


class UploadList(generic.ListView):
    model = userPosts
    queryset = userPosts.objects.order_by("-posted_on")
    template_name = "index.html"
