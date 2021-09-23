from .base import *


def read_secrets(secret_name):
    file = open('/run/secrets/' + secret_name)
    secret = file.read()
    secret = secret.rstrip().lstrip()
    file.close()
    return secret


SECRET_KEY = read_secrets('DJANGO_SECRET_KEY')

DEBUG = False

# 모든 IP에 대해서 접속 허가를 해줌
ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # mariaDB는 mysql에서 나온 산하DB 개념이라 mysql로 설정
        'NAME': 'issactoast',
        'USER': read_secrets('MARIADB_USER'),
        'PASSWORD': read_secrets('MARIADB_PASSWORD'),
        'HOST': 'mariadb', # mariadb 컨테이너 이름
        'PORT': '3306', # mariadb 기본 포트 3306
    }
}