# from .environment import env
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env('DATABASE_NAME'),
#         'USER': env('DATABASE_USER'),
#         'PASSWORD': env('PASSWORD'),
#         'HOST': env('HOST'),
#         'PORT': 5432,
#
#         'ATOMIC_REQUESTS': True,
#     }
# }
from .base import BASE_DIR
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

