from blog.settings import *




SECRET_KEY = 'django-insecure-mq4p@q8tms#&b3$vhaos86*^xsf)s-e+*!yizp71ldf)rce5qd'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'config',
    'widget_tweaks',
    'accounts',
]


ALLOWED_HOSTS = ['127.0.0.1']


DEBUG = True


SITE_ID = 1



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    BASE_DIR / "static",

] 

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_REDIRECT_URL = "/" 
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_TZ = True



