import os

from .config import ENV

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = ENV

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', False)

ALLOWED_HOSTS = [".run.goorm.io", ".herokuapp.com", "juyeonkim.com"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'django_extensions',
    'anymail',
    
    'show',
    'contact',
    'work',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dj_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'dj_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Stroage - Dropbox
DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DROPBOX_ROOT_PATH = '/앱/juyeonkim'
DROPBOX_APP_KEY = env["DROPBOX_APP_KEY"]
DROPBOX_APP_SECRET = env["DROPBOX_APP_SECRET"]
DROPBOX_OAUTH2_REFRESH_TOKEN = env["DROPBOX_OAUTH2_REFRESH_TOKEN"]
# 이제 DROPBOX_OAUTH2_TOKEN 방식은 Dropbox에서 제공하지 않음.
# DROPBOX_OAUTH2_REFRESH_TOKEN을 얻는 방식은 아래 페이지를 참고할 것.
# https://stackoverflow.com/questions/70641660/how-do-you-get-and-use-a-refresh-token-for-the-dropbox-api-python-3-x/71794390#71794390


# mailing - Mailgun
ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": env["MAILGUN_API_KEY"],
    "MAILGUN_API_URL": "https://api.mailgun.net/v3",
    "MAILGUN_SENDER_DOMAIN": env["MAILGUN_SENDER_DOMAIN"],  # your Mailgun domain, if needed
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or...
DEFAULT_FROM_EMAIL = "flyupjy@naver.com"  # if you don't already have this in settings
SERVER_EMAIL = "flyupjy@naver.com"  # ditto (default from-email for Django errors)

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# DEFAULT_FROM_EMAIL = ' flyupjy@naver.com'
ADMIN_EMAILS = [SERVER_EMAIL, 'rukidding918@gmail.com']
# EMAIL_HOST = 'smtp.mailgun.org'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'flyupjy@naver.com'
# EMAIL_HOST_PASSWORD = '4219d9344fba19b4686cdedbff60b04d-31eedc68-13f39772'