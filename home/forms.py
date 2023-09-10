from .models import userPosts, postComments, category
from django import forms

subjects = category.objects.all().values_list('title', 'title')

subject_list = []

for item in subjects:
    subject_list.append(item)

class CommentForm(forms.ModelForm):
    class Meta:
        model = postComments
        fields = ('comment_body',)
        



class UploadForm(forms.ModelForm):
    class Meta:
        model = userPosts
        fields = ('header', 'post_image', 'category', 'caption')

        widgets = {
            'category': forms.Select(choices=subject_list, attrs={'class': 'form-control'})
        }

