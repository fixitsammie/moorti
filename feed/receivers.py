
from django.dispatch import receiver
#from myregistration.views import user_registered
from .models import Campaign,UserProfile

"""
@receiver(user_registered)
def my_campaigncallback(sender,user,request,**kwargs):
	print("Request finished")
	print(user.username)
	campaign=Campaign(title=user.username,slug=user.username,user=user)
	campaign.save()
"""

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        UserProfile.objects.get_or_create(user=kwargs.get('instance'))
    user=kwargs.get('instance')
    campaign=Campaign.objects.get_or_create(title=user.username,slug=user.username,user=user)
    print('we dey alright')
    
