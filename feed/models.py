# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# Create your models here.


class UserProfile(models.Model):
    user=models.OneToOneField(User)
    pic=models.ImageField(upload_to='img/user',blank=True)

    def  __str__(self):
        return self.user.username


class Campaign(models.Model):
    title=models.CharField(max_length=100)
    slug=models.CharField(max_length=150)
    user=models.ForeignKey(User)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    image=models.ImageField(blank=True,upload_to='img/%y/%m/%d')

    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        if not self.id:
            self.slug=slugify(self.title)
        super(Campaign, self).save(*args,**kwargs)


class CampaignResponse(models.Model):
    campaign=models.ForeignKey(Campaign)
    text=models.CharField(max_length=1000)
    created=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.text

class Message(models.Model):
	text=models.CharField(max_length=200)
	created=models.DateField(auto_now_add=True)

	def __str__(self):
		return self.text
