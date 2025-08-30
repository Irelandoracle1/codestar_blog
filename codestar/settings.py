from pathlib import Path
import os
import dj_database_url

# -----------------------
# Base directories
# -----------------------
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# -----------------------
# Quick-start settings
# -----------------------
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-default-key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [
    'bloged-project-88660c5a7dd5.herokuapp.com',
    '127.0.0.1',
]

# -----------------------
# Installed apps
# -----------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third-party apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_summernote',

    # Your apps
    'blog',
    'about',
]

SITE_ID = 1

# Login URLs
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# -----------------------
# Middleware
# -----------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # for Heroku static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # must be after auth
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'codestar.urls'

# -----------------------
# Templates
# -----------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required by allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'codestar.wsgi.application'

# -----------------------
# Database (Heroku Postgres)
# -----------------------
DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get("DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}")
    )
}

# -----------------------
# CSRF
# -----------------------
CSRF_TRUSTED_ORIGINS = [
    "https://*.herokuapp.com",
]

# -----------------------
# Password validation
# -----------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------
# Allauth settings
# -----------------------
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = False

# -----------------------
# Internationalization
# -----------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------
# Static files
# -----------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise configuration for Heroku
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -----------------------
# Default primary key field type
# -----------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------
# Email backend for debugging
# -----------------------
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
