# Create your views here.
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import RegistrationForm,LoginForm
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.template import RequestContext
from django.template import Context
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect
from django.shortcuts import  redirect

from django.contrib.auth.decorators import login_required

from django.dispatch import Signal

from django.contrib import messages
from django.utils.translation import ugettext as _
"""
#from forum.models import UserProfile
user_registered = Signal(providing_args=["user", "request"])

user_registered.send(sender=User,
                                     user=user,
                                     request=request)
            
"""

def register_page(request,template_name="registration/register.html"):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method=='POST':
        form=RegistrationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            form.save()
            
            user = authenticate(username=username, password=password)
            #UserProfile(user=user).save()
            user.save()
            login(request, user)
            return redirect('/')
        else:
            
            return render(request,template_name,context={'form':form})
    else:
        form=RegistrationForm()
        variables= {'form':form}
        return render(request,template_name,context=variables)

def login_request(request,template_name="registration/login.html"):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            person=authenticate(username=username,password=password)
            if person is not None:
                login(request, person)
                return HttpResponseRedirect('/')
            else:
                return render(request,template_name, context={'form':form})
        else:
            return render(request,template_name, context={'form':form})
    else:
        """user is not submitting the form, show the login form"""
        form=LoginForm()
        context={'form':form}
        return render(request,template_name,context)

@login_required
def logout_request(request):
    context = RequestContext(request)
    logout(request)
    messages.add_message(request,messages.INFO,_('You are logged out.'))
    return HttpResponseRedirect('/')
    
 
    
