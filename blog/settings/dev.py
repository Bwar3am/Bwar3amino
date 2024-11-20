from blog.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mq4p@q8tms#&b3$vhaos86*^xsf)s-e+*!yizp71ldf)rce5qd'


DEBUG = True

ALLOWED_HOSTS = []

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
