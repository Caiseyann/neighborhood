from django.test import TestCase
from .models import *

# Create your tests here.


class ProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='test')
        self.profile = Profile.objects.create(
            user=self.user, email='example@samplemail.com', contact='mycontact')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_get_all_profiles(self):
        self.profile.save()
        profile = Profile.get_all_profiles()
        self.assertTrue(len(profile) > 0)

    def test_find_profile(self):
        self.profile.save()
        profile = Profile.find_profile('cheru')
        self.assertTrue(len(profile) > 0)


class NeighborhoodTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='test')
        self.profile = Profile.objects.create(
            user=self.user, email='example@samplemail.com', contact='mycontact')

        self.strip = Neighborhood.objects.create(locality='locality', user_profile=self.user,
                                                name='strip_name', occupants_count=50)

    def test_instance(self):
        self.assertTrue(isinstance(self.strip, Neighborhood))

    def test_all_hoods(self):
        self.strip.save()
        strip = Neighborhood.all_neighborhoods()
        self.assertTrue(len(strip) > 0)


class BusinessTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='test')
        self.profile = Profile.objects.create(
            user=self.user,email='example@samplemail.com', contact='mycontact')

        self.business = Business.objects.create(name='mpesa',
                                           description='available and reliable', email='example@samplemail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_get_neighborhood_businesses(self):
        self.business.save()
        business = Business.get_neighborhood_businesses(business_strip)
        self.assertTrue(len(business) > 0)

    def test_search_business(self):
        self.business.save()
        business = Business.search_by_name('mpesa')
        self.assertTrue(len(business) > 0)


class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='test')
        self.profile = Profile.objects.create(
            user=self.user, email='example@samplemail.com', contact='mycontact')

        self.post = Post.objects.create(name='sample_post',
                                        image='images/', description='desc')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_all_posts(self):
        self.post.save()
        post = Post.all_posts(id)
        self.assertTrue(len(post) > 0)

    def test_search_post(self):
        self.post.save()
        post = Post.search_by_name('sample_post')
        self.assertTrue(len(post) > 0)
