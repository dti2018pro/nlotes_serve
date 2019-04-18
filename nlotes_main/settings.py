"""
Django settings for nlotes_main project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import dj_database_url
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w9qzdp$^_-3!o$o^78)=pp291ma!ma+41dg=zmg3*&s6$i$vv#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Disable Django's own staticfiles handling in favour of WhiteNoise, for
    # greater consistency between gunicorn and `./manage.py runserver`. See:
    # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    # 'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    'django.contrib.admindocs',
    'django.contrib.sites',  # new

    # 3rd party
    'allauth',  # new
    'allauth.account',  # new
    'allauth.socialaccount',  # new
    'allauth.socialaccount.providers.google',  # new
    'crispy_forms',

    # aggregated
    'rest_framework',
    'corsheaders',
    'django_filters',
    #'rest_framework.authtoken',
    'rest_framework.authtoken',
    # Local
    #'accounts',
    'users',
    'home',

    'catalogo',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

if DEBUG:
    INSTALLED_APPS = INSTALLED_APPS + [
        'debug_toolbar',
    ]
    MIDDLEWARE = MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

ROOT_URLCONF = 'nlotes_main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],

        },
    },
]

WSGI_APPLICATION = 'nlotes_main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASESx = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd4ejj9822e8v7e',
        'USER': 'leazvhzuinglqr',
        'PASSWORD': '4c95bbf3d027d650b2cc3f2c07670ad78ee42a9a15d1d1ccb080200472737fb9',
        'HOST': 'ec2-54-225-76-201.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

#####


# Change 'default' database configuration with $DATABASE_URL.
DATABASES['default'].update(dj_database_url.config(
    conn_max_age=500, ssl_require=True))

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


#
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
# END MEDIA CONFIGURATION


# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Activate Django-Heroku.
django_heroku.settings(locals())


# Bootstrap Crispy-Forms settings
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# django-debug-toolbar settings
INTERNAL_IPS = ['127.0.0.1']


LOGIN_REDIRECT_URL = '/admin/'
#LOGOUT_REDIRECT_URL = '/accounts/login/'

AUTH_USER_MODEL = 'users.User'

# EMAIL
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'upeu2018pro@gmail.com'
EMAIL_HOST_PASSWORD = '123456782018'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'upeu2018pro@gmail.com'

# https://wsvincent.com/django-user-authentication-tutorial-password-reset/
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    #'accounts.authentication.EmailAuthBackend',
    #'oauth2_provider.backends.OAuth2Backend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

# DJANGO-ALLAUTH SETTINGS
# Site id required for using 'sites' framework with django-allauth
SITE_ID = 1

#ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_USERNAME_REQUIRED = False
# http://django-allauth.readthedocs.io/en/latest/configuration.html
# https://wsvincent.com/
# https://github.com/wsvincent/djangox/blob/master/djangox/settings.py
#LOGIN_REDIRECT_URL = 'admin'
#ACCOUNT_LOGOUT_REDIRECT_URL = 'admin'
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

# Don't collect usernames, use email instead
# ACCOUNT_USER_MODEL_USERNAME_FIELD (='username') # NO haga
# ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
# default is 'True', use 'optional' for development purposes
#ACCOUNT_EMAIL_VERIFICATION = 'optional'

ACCOUNT_UNIQUE_EMAIL = True
# SOCIALACCOUNT_PROVIDERS
# default is 'True', only force user to enter password once
# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

# controls life time of the session, default is 'None' to ask user
# "Remember me?"
ACCOUNT_SESSION_REMEMBER = True


# Perosnalizando forms
# SOCIALACCOUNT_AUTO_SIGNUP = False
# SOCIALACCOUNT_FORMS = {
#    'signup': 'users.forms.MyCustomSocialSignupForm',
# }

# ACCOUNT_ADAPTER="foo_app.adapters.FooAppAccountAdapter"
SOCIALACCOUNT_ADAPTER = "users.adapters.MySocialAccountAdapter"

ACCOUNT_FORMS = {'signup': 'users.forms.MyCustomSignupForm'}
#ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.SignupForm'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'mysite.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'MYAPP': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True