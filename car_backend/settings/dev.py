from car_backend.settings.common import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'car_backend',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD':'123456',
    }
}

ALLOWED_HOSTS = ['127.0.0.1','localhost']
