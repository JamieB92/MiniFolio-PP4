from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic.edit import UpdateView
from .models import userPosts
from .models import postComments
from .forms import CommentForm
from .forms import UploadForm
from .forms import EditForm

# Landing Page
class LandingPage(View):
    def get(self, request):
        return render(request, "index.html")

# Home page that shows all posts uploaded by users 
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

# Create a new post 
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

    def post(self, request,):
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload = upload_form.save(commit=False)
            upload.creator = request.user
            upload.save()
            return redirect('home')

        return render(
            request,
            "upload-post.html",
            {
                "upload_form": upload_form,
            },
        )

#  Edit a Post
class EditPost(generic.UpdateView):
    model = userPosts
    fields = ["header", "post_image", "caption"]
    template_name = "edit-post.html"
    success_url = 'home'

    

# Post a comment to a post 
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
