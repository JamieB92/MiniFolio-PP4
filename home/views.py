from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import userPosts
from .models import postComments
from .forms import CommentForm
from .forms import UploadForm


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
            }
        )


class UploadPost(View):

    def get(self, request):
        upload_form = UploadForm(data=request.POST)
        return render(
            request,
            "upload-post.html",
            {
                "upload_form": upload_form,
            },
        )

    def post(self, request):

        post = get_object_or_404(post.creator)
        upload_form = UploadForm(data=request.POST)
        if upload_form.is_valid():
            upload_form.instance.name = request.user.username
            upload = upload_form.save(commit=False)
            upload.userPosts = post
            upload.save()
            return redirect('home')
        else:
            upload_form = UploadForm()

        return render(
            request,
            "home.html",
            {
                "upload_form": upload_form,
            },
        )


class PostComment(View):

    def get(self, request, pk):
        comment_form = CommentForm(data=request.POST)
        return render(
            request,
            "post-comment.html",
            {
                "comment_form": comment_form,
            },
        )

    def post(self, request, pk):

        post = get_object_or_404(userPosts, pk=pk)
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post_comments = post
            comment.save()
            return redirect('home')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "home.html",
            {
                "comment_form": comment_form,
            },
        )
