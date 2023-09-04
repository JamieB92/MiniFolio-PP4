from . import views
from django.urls import path
from .views import EditPost 
from .views import DeletePost


urlpatterns = [
    path('home/', views.UploadList.as_view(), name="home"),
    path('', views.LandingPage.as_view(), name="landing"),
    path('post-comment/<int:pk>', views.PostComment.as_view(), name="post-comment"),
    path('upload-post', views.UploadPost.as_view(), name="upload-post"),
    path('edit-post/<int:pk>', EditPost.as_view(), name="edit-post"),
    path('<int:pk>/delete-post', DeletePost.as_view(), name="delete-post"),
]
