from . import views
from django.urls import path

urlpatterns = [
    path('', views.UploadList.as_view(), name="home"),
]
