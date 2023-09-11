from . import views
from django.urls import path
from .views import EditPost, DeletePost, PostSuperLike, PostUpVoted
from .views import CategoryView, AllCategories, PostDownVoted


urlpatterns = [
    path('home/', views.UploadList.as_view(), name="home"),
    path('', views.LandingPage.as_view(), name="landing"),
    path('post-comment/<int:pk>',
         views.PostComment.as_view(), name="post-comment"),
    path('upload-post', views.UploadPost.as_view(), name="upload-post"),
    path('edit-post/<int:pk>', EditPost.as_view(), name="edit-post"),
    path('<int:pk>/delete-post', DeletePost.as_view(), name="delete-post"),
    path('super-vote/<int:pk>', PostSuperLike, name='super-vote'),
    path('up-vote/<int:pk>', PostUpVoted, name='up-vote'),
    path('down-vote/<int:pk>', PostDownVoted, name='down-vote'),
    path('category/<str:subject>/', CategoryView, name='category'),
    path('categories/', views.AllCategories.as_view(), name="categories"),
]
