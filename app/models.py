from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime as dt

# Create your models here.
class Profile(models.Model):
    avatar = models.ImageField(upload_to='images/', blank=True)
    contact = HTMLField()
    email = models.EmailField(max_length=80, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    objects = models.Manager()

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def find_profile(cls, search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    class Meta:
        ordering = ['user']


class Neighborhood(models.Model):
    locality = models.CharField(
        max_length=30, default="e.g Nairobi, Mombassa, Naivasha etc")
    name = models.CharField(max_length=30)
    occupants_count = models.IntegerField(default=0, blank=True)
    # profile=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    user_profile = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='strip', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    

    @classmethod
    def search_neighborhood_by_name(cls, search_term):
        neighborhoods = cls.objects.filter(name__icontains=search_term)
        return neighborhoods

    @classmethod
    def one_neighborhood(cls, id):
        neighborhood = Neighborhood.objects.filter(id=id)
        return neighborhood

    @classmethod
    def all_neighborhoods(cls):
        neighborhoods = cls.objects.all()
        return neighborhoods

    @classmethod
    def get_neighborhood_by_id(cls, id):
        neighborhood = Neighborhood.objects.filter(id=Neighborhood.id)
        return neighborhood

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile




