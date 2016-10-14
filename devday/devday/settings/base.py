"""
Django settings for devday project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import os
from django.core.exceptions import ImproperlyConfigured

gettext = lambda s: s


def get_env_variable(var_name):
    """
    Get a setting from an environment variable.

    :param str var_name: variable name

    """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable('DEVDAY_SECRET')

ALLOWED_HOSTS = []

DATA_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Application definition

ROOT_URLCONF = 'devday.urls'

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'devday', 'static'),
)
SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'devday', 'templates'), ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]

MIDDLEWARE_CLASSES = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'devday',
    'attendee',
    'talk',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'reversion',
    'crispy_forms',
    'django_file_form',
    'django_file_form.ajaxuploader',
]

AUTH_USER_MODEL = 'attendee.devdayuser'

LANGUAGES = (
    ('de', gettext('de')),
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    1: [
        {
            'code': 'de',
            'name': gettext('de'),
            'public': True,
            'hide_untranslated': False,
            'redirect_on_fallback': True,
        },
        {
            'code': 'en',
            'name': gettext('en'),
            'public': False,
            'hide_untranslated': False,
            'redirect_on_fallback': True,
        },
    ],
    'default': {
        'fallbacks': ['de'],
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ('devday_index.html', 'DevDay Startseite'),
    ('devday.html', 'Devday'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DEVDAY_PG_DBNAME'),
        'USER': get_env_variable('DEVDAY_PG_USER'),
        'PASSWORD': get_env_variable('DEVDAY_PG_PASSWORD'),
        'HOST': get_env_variable('DEVDAY_PG_HOST'),
        'PORT': get_env_variable('DEVDAY_PG_PORT'),
    }
}

CMS_STYLE_NAMES = (
    # styles for bootstrap grid model
    ('row', gettext('row')),
    ('container', gettext('container')),
    ('col-xs-12', gettext('col-xs-12')),
    ('col-md-12', gettext('col-md-12')),
)

MIGRATION_MODULES = {

}

# settings for django-registration
# see: https://django-registration.readthedocs.io/en/2.1.1/index.html
ACCOUNT_ACTIVATION_DAYS = 14

CRISPY_TEMPLATE_PACK = 'bootstrap3'

TALK_THUMBNAIL_HEIGHT = 320
