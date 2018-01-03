# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response,render
from django.template import RequestContext,Context,Template
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
import datetime
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Campaign,CampaignResponse,UserProfile
from .forms import CampaignForm


def home(request):
    
    time=datetime.datetime.now()
    threads=[]
    categories=[]
    if request.user.is_authenticated:
        campaigns=Campaign.objects.filter(user=request.user).order_by('-created')
        variables={'campaigns':campaigns}
        return render(request,'pages/logged_index.html',context=variables)
    else:
        variables={'threads':threads,'categories':categories,'time':time}
        return render(request,'pages/index.html',context=variables)




from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def get_campaign(request,slug):
    try:
        campaign=Campaign.objects.get(slug=slug)
    except:
        raise Http404('Does not exist')
    if request.POST:
        form=CampaignForm(request.POST)
        if form.is_valid():
            campaign_response=CampaignResponse(campaign=campaign,text=request.POST['opinion'])
            campaign_response.save()
            messages.add_message(request,messages.SUCCESS,'Your response has been sent successfully')
            return HttpResponseRedirect('/')
        else:
            form=CampaignResponse(request.POST)
    else:
        form=CampaignForm()
    variables={'campaign':campaign,'form':form}
    return render(request,'show_campaign.html',context=variables)

@login_required
def get_campaign_responses(request,slug):
    try:
        campaign=Campaign.objects.get(slug=slug)
    except:
        raise Http404('Does not exist')
    if campaign.user!=request.user:
        raise Http404('You are not authorized to view this page')
    campaign_response=CampaignResponse.objects.filter(campaign=campaign)
    variables={'campaign':campaign,'campaign_response':campaign_response}
    return render(request,'pages/campaign_responses.html',context=variables)

@login_required
def edit_user_page(request,username):
    if User.objects.filter(username=username).exists() and username==request.user.username:
        user=User.objects.get(username=username)
    else:
        raise Http404('You are not authorized to view this page')
            
    if request.method=='POST':
        first_name=request.POST.get('first_name','')
        last_name=request.POST.get('last_name','')
        email=request.POST.get('email','')
        pic=request.FILES.get('dp','')
        if pic:
            if user.userprofile.id:
                user.userprofile.pic=pic
                user.userprofile.save()
                messages.add_message(request,messages.SUCCESS,_('Profile picture updated'))
            else:
                UserProfile(user=user,pic=pic).save()
        if email and user.email!=email and email != '':
            print("got here")
            user.email=email
            user.save()
            messages.add_message(request,messages.SUCCESS,_('Changes saved'))
        if last_name and user.last_name!=last_name and last_name!='':
            user.last_name=last_name
            user.save()
            messages.add_message(request,messages.SUCCESS,_('Changes saved'))
        if first_name and user.first_name!=last_name and first_name!='':
            user.first_name=first_name
            user.save()
            messages.add_message(request,messages.SUCCESS,_('Changes saved'))
        variables={'last_name':last_name,'email':email}
        return render(request,'edit_user_page.html',context=variables)

    elif request.method=='GET' :
        variables={}
        return render(request,'edit_user_page.html',context=variables)

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect

from social_django.models import UserSocialAuth

@login_required
def settings(request):
    user = request.user
    

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'password.html', {'form': form})

