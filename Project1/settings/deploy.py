from .base import *

env_list = {}
local_env = open(os.path.join(BASE_DIR, '.env'))

while True:
    line = local_env.readline()
    if not line:
        break
    line = line.replace('\n', '')
    start = line.find('=')
    key = line[:start]
    val = line[start+1:]
    env_list[key] = val

SECRET_KEY = env_list['SECRET_KEY']

DEBUG = False

# 모든 IP에 대해서 접속 허가를 해줌
ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # mariaDB는 mysql에서 나온 산하DB 개념이라 mysql로 설정
        'NAME': 'issactoast',
        'USER': 'issactoast',
        'PASSWORD': 'coramdeo96!',
        'HOST': 'mariadb', # mariadb 컨테이너 이름
        'PORT': '3306', # mariadb 기본 포트 3306
    }
}