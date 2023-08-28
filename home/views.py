from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import userPosts
from .models import postComments


class LandingPage(View):
    def get(self, request):
        return render(request, "index.html")


class UploadList(generic.ListView):
    model = userPosts, postComments
    queryset = userPosts.objects.order_by("-posted_on")
    template_name = "home.html"
