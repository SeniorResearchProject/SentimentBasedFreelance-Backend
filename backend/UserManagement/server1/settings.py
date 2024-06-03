"""
Django settings for server1 project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--=o))g*)tsqaoa3f!mo4q7-$0nmk6xj2@jv@)@we1z_&-=!boh'

JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'django-insecure--=o))g*)tsqaoa3f!mo4q7-$0nmk6xj2@jv@)@we1z_&-=!boh')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
ALLOWED_HOSTS = [
    'usermanagement-qtjm.onrender.com',
    'your_other_domains_or_ips_if_any',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'users',
    'social_auth',
    'payment'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'server1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blrnwyzda4uayq4pqwme',
        'USER': 'uzjoeb37cweaur3d',
        'PASSWORD': 'W0PqxyQnXQteTHz1aviy',
        'HOST': 'blrnwyzda4uayq4pqwme-mysql.services.clever-cloud.com',
        'PORT': '3306',
    }
}

REST_FRAMEWORK={
    'NON_FIELD_ERRORS_KEY': 'error'
}


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# email info
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
# EMAIL_HOST_USER= os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_USER= 'meklitadugna566@gmail.com'
# EMAIL_HOST_PASSWORD= os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST_PASSWORD='kjykryfpgwqburhu'


#stripe
STRIPE_PUBLIC_KEY = 'pk_test_51P9pg2LCYw4uR7bJyugyAPZlfdOEWRpv6h0DYneGbGuw96VprlwBfE96sBeLWCTu952pVWQCDNALF9GSDB9YKa5q00kcUmv0ET'
STRIPE_SECRET_KEY = 'sk_test_51P9pg2LCYw4uR7bJcHvjiZvKzaYP5DS9bzlnCnPmzJK8kXRyzpEjRycTHJdoOzdy3zH3jSc8Gdsq1q3T408w2Nbe00v7DYHzYW'
STRIP_WEBHOOK_SECRET = 'whsec_08a8faf549c09a608202be18602580ba0ef2357ccb0e60961b1125b146978b3d'
PRODUCT_PRICE = 'price_1PA4jPLCYw4uR7bJ0wWXteRp'

REDIRECT_DOMAIN = 'http://127.0.0.1:8000'

#google
GOOGLE_CLIENT_ID = '92149831690-ojqrq5a886l2n666mq1lajhgqguf03jp.apps.googleusercontent.com'

#Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Add this if you have project-wide templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Add this line
                'django.contrib.auth.context_processors.auth',  # Add this line
                'django.contrib.messages.context_processors.messages',  # Add this line
            ],
        },
    },
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',  # default
#     'users.backends.EmailBackend',  # path to your EmailBackend class
# ]



