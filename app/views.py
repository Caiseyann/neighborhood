from django.shortcuts import render
from .models import *
from .forms import *
from .models import *
from .forms import *
from .email import *
from .email import send_welcome_email
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def homepage(request):
    if request.user.is_authenticated:
        if Join.objects.filter(user_id=request.user).exists():
            strip = Neighborhood.objects.get(pk=request.user.join.strip_id.id)
            posts = Post.objects.filter(post_strip=request.user.join.strip_id.id)
            businesses = Business.objects.filter(
                business_strip=request.user.join.strip_id.id)
            return render(request, 'current_strip.html', {"strip": strip, "businesses": businesses, "posts": posts})
        else:
            strips = Neighborhood.all_neighborhoods()
            return render(request, 'index.html', {"strips": strips})
    else:
        strips = Neighborhood.all_neighborhoods()
        return render(request, 'index.html', {"strips": strip})


@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('homepage')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})

def add_strip(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddStripForm(request.POST, request.FILES)
        if form.is_valid():
            strip = form.save(commit=False)
            strip.user_profile = current_user
            strip.save()
        return redirect('homepage')

    else:
        form = AddStripForm()
    return render(request, 'add_strip.html', {"form": form})

@login_required(login_url='/accounts/login/')
def add_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.business_owner = current_user
            business.business_strip = request.user.join.strip_id
            business.save()
        return redirect('homepage')

    else:
        form = AddBusinessForm()
    return render(request, 'add_business.html', {"form": form})


@login_required(login_url='/accounts/login/')
def join_strip(request, strip_id):
    '''
    This view function will implement adding 
    '''
    neighborhood = Neighborhood.objects.get(pk=strip_id)
    if Join.objects.filter(user_id=request.user).exists():

        Join.objects.filter(user_id=request.user).update(strip_id=neighborhood)
    else:

        Join(user_id=request.user, strip_id=neighborhood).save()

    return redirect('homepage')


@login_required(login_url='/accounts/login/')
def leave_strip(request, strip_id):
    '''
    This function will delete a neighbourhood instance in the join table
    '''
    if Join.objects.filter(user_id=request.user).exists():
        Join.objects.get(user_id=request.user).delete()
        return redirect('homepage')


@login_required(login_url='/accounts/login/')
def user_profile(request, username):
    profile = User.objects.get(username=username)
    try:
        profile_info = Profile.get_profile(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)
    businesses = Business.get_profile_businesses(profile.id)
    title = f'@{profile.username}'
    return render(request, 'profile.html', {'title': title, 'profile': profile, 'profile_info': profile_info, 'businesses': businesses})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.poster = current_user
            post.post_strip = request.user.join.strip_id
            post.save()
        return redirect('homepage')

    else:
        form = AddPostForm()
    return render(request, 'new_post.html', {"form": form})

def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        business_results = Business.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "businesses": business_results})

    else:
        message = "Please enter a search term"
        return render(request, 'search.html', {"message": message})
