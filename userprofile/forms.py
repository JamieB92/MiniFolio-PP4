from django import forms
from .models import userProfiles


class ProfileForm(forms.ModelForm):
    class Meta:
        model = userProfiles
        fields = ('profile_image', 'profile_bio')