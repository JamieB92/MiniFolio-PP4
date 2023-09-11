from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from .models import userPosts, postComments, User, category
from .forms import CommentForm, UploadForm


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
    success_url = "/home"

# Delete A Post


class DeletePost(DeleteView):
    model = userPosts
    success_url = "/home"
    template_name = "delete-post.html"

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


class PostSuperLike(View):

    def post(self, request, pk):
        posts = userPosts.objects.get(id=pk)
        user = User.objects.get(id=request.user.id)

        liked = userPosts.objects.filter(super_vote__id__in=[user.id])

        if liked:
            posts.super_vote.remove(request.user)
        else:
            posts.super_vote.add(request.user)

        return HttpResponseRedirect(reverse('home'))


class PostUpVoted(View):

    def post(self, request, pk):
        posts = userPosts.objects.get(id=pk)
        user = User.objects.get(id=request.user.id)

        upVoted = userPosts.objects.filter(up_vote__id__in=[user.id])

        if upVoted:
            posts.up_vote.remove(request.user)
        else:
            posts.up_vote.add(request.user)

        return HttpResponseRedirect(reverse('home'))


class PostDownVoted(View):

    def post(self, request, pk):
        posts = userPosts.objects.get(id=pk)
        user = User.objects.get(id=request.user.id)

        downVoted = userPosts.objects.filter(down_vote__id__in=[user.id])

        if downVoted:
            posts.down_vote.remove(request.user)
        else:
            posts.down_vote.add(request.user)

        return HttpResponseRedirect(reverse('home'))


# Specific Categories View

def CategoryView(request, subject):

    post_subjects = userPosts.objects.filter(category=subject)

    return render(request, 'specific-categories.html',
                  {'subject': subject.title(), 'post_subjects': post_subjects})


# All Categories

class AllCategories(generic.ListView):
    model = userPosts
    template_name = 'all-categories.html'
    subject = category.objects.all()

    def get_context_data(self, *args, **kwargs):
        subject_menu = category.objects.all()
        context = super(AllCategories, self).get_context_data(*args, **kwargs)
        context["subject_menu"] = subject_menu
        return context
