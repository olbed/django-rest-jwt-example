"""
Django settings for project project.
Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/

Quick-start development settings - unsuitable for production
https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
"""

from os import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Environment

DEBUG = environ.get("DEBUG") == "TRUE"

if DEBUG:
    # Local dev server settings
    SECRET_KEY = "5%#7%@bv3s8ob)$rbsg_@m*@9y^=&!cp0)e4od_lh$l5a7mc40"
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

else:
    # Production settings
    SECRET_KEY = environ.get("SECRET_KEY")
    ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",  # required by allauth
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",  # required by allauth
    "django.contrib.staticfiles",
    "django.contrib.sites",  # required by allauth
    # 3rd party
    "rest_framework",
    "rest_framework.authtoken",  # required by dj_rest_auth to enable registration
    "allauth",  # required by dj_rest_auth to enable registration
    "allauth.account",  # required by dj_rest_auth to enable registration
    "allauth.socialaccount",  # required by dj_rest_auth to enable registration
    "dj_rest_auth",  # provides authentication endpoints
    "dj_rest_auth.registration",  # provides registration endpoint
    # local
    "accounts.apps.AccountsConfig",  # custom User model
    "snippets.apps.SnippetsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


#######################
# Applications config #
#######################

# django.contrib.auth
AUTH_USER_MODEL = "accounts.User"  # to make emails unique and usernames not required
AUTHENTICATION_BACKENDS = ("allauth.account.auth_backends.AuthenticationBackend",)

# django.contrib.sites
SITE_ID = 1

# rest_framework
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # For browsable API login button
        "rest_framework.authentication.SessionAuthentication",
        # For API frontends (JWT tokens)
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

# allauth
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"

# dj_rest_auth
REST_USE_JWT = True
JWT_AUTH_COOKIE = "token"
