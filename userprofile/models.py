from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from home.models import userPosts
from home.models import postComments


class userProfiles(models.Model):

    profile_image = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False,
                             blank=False, related_name='user_profile')
    profile_bio = models.TextField(max_length=350, blank=True, null=True)


def __str__(self):
    return str(self.user)


def users_post(self):
    return self.creator.all()
