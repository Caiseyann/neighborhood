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


