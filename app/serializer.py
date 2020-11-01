from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user','profile_photo','contact')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields =('id','title',)
