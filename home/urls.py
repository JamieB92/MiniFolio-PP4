from . import views
from django.urls import path


urlpatterns = [
    path('home/', views.UploadList.as_view(), name="home"),
    path('', views.LandingPage.as_view(), name="landing"),
    path('post-comment/<int:pk>', views.PostComment.as_view(), name="post-comment"),
]
