# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class FeedConfig(AppConfig):
    name = 'feed'

    def ready(self):
    	from .import receivers
