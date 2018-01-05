"""
Django settings for moorti project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*!27o7o*tn(q6^5wzluezb6ac*7d#t&q7q3)@#f#@6vz+(90o%'

SITE_ID = 1
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1','moorti.me','www.moorti.me','moorti.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'feed.apps.FeedConfig',
    'myregistration',
    'social_django',
    'storages',
   
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    
]

ROOT_URLCONF = 'moorti.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'social_django.context_processors.backends',  
                'social_django.context_processors.login_redirect',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'moorti.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases



DATABASES = {
    'default': {
        'NAME': 'dbpostgresmoorti',
        'ENGINE': 'django.db.backends.postgresql',
        'HOST':'moortipostgresone.czwdkshkx0py.us-east-2.rds.amazonaws.com:5432',
        'USER': 'moortiusernameone',
        'PASSWORD': 'moortinipassword'
    },
    'local': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/



STATIC_ROOT= os.path.join(BASE_DIR, "staticfiles")

AWS_ACCESS_KEY_ID = 'AKIAI5DK3TRZNPR6PJAA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'moortistaticassetsbucket'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'


#STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),

 
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEFAULT_FILE_STORAGE = 'moorti.storage_backends.MediaStorage'

MEDIA_URL = '/media/'

MEDIA_ROOT= os.path.join(BASE_DIR, "media")

LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_TWITTER_KEY = '9TD12xahCWCDdyLzpmw61GSM9'
SOCIAL_AUTH_TWITTER_SECRET = 'mwtdcUe4uOvvJjDk2AuQ9Mq2xiHPw3740m5iGLf6hwg3B4TNSx'
#SOCIAL_AUTH_FACEBOOK_KEY="135569913790943"
#SOCIAL_AUTH_FACEBOOK_SECRET= "0b5c5f3cbf684f62eaba7adac12db9cc"
SOCIAL_AUTH_FACEBOOK_KEY="204577913446792"
SOCIAL_AUTH_FACEBOOK_SECRET="fe2d6a8042f1b407324c16d9b8a99359"
SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/settings/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False
SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.10'
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile'],  # user need not share user_friends     
        'AUTH_PARAMS': {'auth_type': 'rerequest'},  # automatic login after oauth signup done
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'en_US',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.10',        
    },
   
}


#moortinipassword
#database_name:dbpostgresmoorti
db_name='dbpostgresmoorti'
db_username='moortiusernameone'
end_point_db='moortipostgresone.czwdkshkx0py.us-east-2.rds.amazonaws.com'
db_port=5432
