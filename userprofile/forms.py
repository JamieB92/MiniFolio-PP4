from .models import userProfiles
from django import forms

class ProfileForm(forms.ModelForm):
  

    class Meta:
        model = userProfiles
        fields = [
            "profile_image"
            "profile_bio",
        ]