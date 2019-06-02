from .base import *

DEBUG = False

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static', 'dist')
]