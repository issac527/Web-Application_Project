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

DEBUG = True

# 모든 IP에 대해서 접속 허가를 해줌
ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}