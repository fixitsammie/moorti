"""feedbackloop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from feed import views


from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

url(r'^$', views.home, name='home'),
url(r'^oauth/', include('social_django.urls', namespace='social')),
 
    url(r'^admin/', admin.site.urls),
url(r'^settings/$', views.settings, name='settings'),
    url(r'^settings/password/$', views.password, name='password'),
     url(r'', include('myregistration.urls')),
url(r'^(?P<slug>[-\w]+)/$',views.get_campaign,name='get_campaign'),
url(r'^(?P<slug>[-\w]+)/view/$',views.get_campaign_responses,name='get_campaign_responses'),
url(r'^(?P<username>\w+)/edit/$',views.edit_user_page,name='edit_user_page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


