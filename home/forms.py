from .models import postComments
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = postComments
        fields = ('comment_body',)
