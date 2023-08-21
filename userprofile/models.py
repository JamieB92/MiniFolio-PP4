from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from home.models import userPosts


class userProfiles(models.Model):

    profile_image = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False,
                             blank=False, related_name='user_profile')
    username = models.CharField(max_length=30, blank=True, null=True)
    profile_bio = models.TextField(max_length=350, blank=True)


def __str__(self):
    return str(self.user)


def users_post(self):
    return self.creator.all()
