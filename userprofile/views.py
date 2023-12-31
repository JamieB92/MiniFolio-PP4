from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .models import userPosts
from .models import postComments
from .models import userProfiles
from .forms import ProfileForm
from .forms import EditProfile


class UserProfile(ListView):

    def get(self, request, pk):
        profile = userProfiles.objects.get(user=pk)
        myposts = userPosts.objects.order_by("-posted_on")
        comments = postComments.objects.order_by("-created_on")
        return render(
            request, 'profile.html',
            {   'comments': comments,
                'profile': profile,
                'myposts': myposts,
            }
            )


class CreateUserProfile(CreateView):

    def get(self, request):
        profile_form = ProfileForm(data=request.POST)
        return render(
            request,
            "create-profile.html",
            {
                "profile_form": profile_form,
            },
        )

    def post(self, request):
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')

        return render(
            request,
            "create-profile.html",
            {
                "profile_form": profile_form,
            },
        )


class EditMyProfile(UpdateView):

    model = userProfiles
    fields = ["profile_image", "profile_bio"]
    template_name = "edit-profile.html"
    success_url = "/home"
