from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# DB Model for User Posts
class userPosts(models.Model):
    header = models.CharField(max_length=100, unique=True)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="creator_posts")
    posted_on = models.DateTimeField(auto_now_add=True)
    post_image = CloudinaryField('image')
    caption = models.TextField(max_length=500)
    super_vote = models.ManyToManyField(
        User, related_name='post_super_votes', blank=True)
    up_vote = models.ManyToManyField(
        User, related_name='post_up_votes', blank=True)
    down_vote = models.ManyToManyField(
        User, related_name='post_down_votes', blank=True)

    class Meta:
        ordering = ["-posted_on"]
        verbose_name_plural = "User Posts"

    def __str__(self):
        return self.header

    # Counts for Super, Up and Down Votes

    def total_up_votes(self):
        return self.up_vote.count()

    def total_super_vote(self):
        return self.super_vote.count()

    def total_down_vote(self):
        return self.down_vote.count()

# DB Model for posts comments


class postComments(models.Model):
    post_comments = models.ForeignKey(userPosts, on_delete=models.CASCADE,
                                      related_name="post_comments")
    name = models.CharField(max_length=80)
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
        verbose_name_plural = "Post Comments"

    def __str__(self):
        return f"Comment {self.comment_body} by {self.name}"
