from .base import *

# 서버 환경

ALLOWED_HOSTS = ['3.35.43.149']

# set default path of static file
STATIC_ROOT = BASE_DIR / 'static/' # /home/ubuntu/projects/mysite
STATICFILES_DIRS = [] # 오류 방지용

DEBUG = False