from . import views
from django.urls import path
from .views import UserProfile
from .views import CreateUserProfile


urlpatterns = [
    path('profile/<int:pk>', UserProfile.as_view(), name="profile"),
    path('create-profile', CreateUserProfile.as_view(), name="create-profile"),
]