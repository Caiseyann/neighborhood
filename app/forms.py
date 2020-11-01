from django import forms
from .models import *

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class AddStripForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['user_profile', 'profile']


class AddBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['business_owner', 'business_strip']

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['poster', 'post_strip']
