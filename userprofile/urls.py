from . import views
from django.urls import path
from .views import UserProfile
from .views import CreateUserProfile
from .views import EditMyProfile


urlpatterns = [
    path('profile/<int:pk>', UserProfile.as_view(), name="profile"),
    path('create-profile', CreateUserProfile.as_view(), name="create-profile"),
    path('edit-profile/<int:pk>', EditMyProfile.as_view(),
         name="edit-profile"),
]
