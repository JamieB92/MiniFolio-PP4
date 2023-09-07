from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import userPosts
from .models import userProfiles
from .forms import ProfileForm


class UserProfile(ListView):
    model = userProfiles
    template_name = "profile.html"

    def get_profile(self):
        return self.request.user


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