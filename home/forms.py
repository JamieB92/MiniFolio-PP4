from .models import userPosts
from .models import postComments
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = postComments
        fields = ('comment_body',)


class UploadForm(forms.ModelForm):
    class Meta:
        model = userPosts
        fields = [
            "header",
            "post_image",
            "caption",
        ]
