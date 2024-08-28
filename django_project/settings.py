import socket
from pathlib import Path
from environs import Env

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env("DJANGO_SECRET_KEY")
DEBUG = env.bool("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', '".herokuapp.com', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "django.contrib.sites",

    "crispy_forms",
    "crispy_bootstrap5",
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    "debug_toolbar",
    'django_extensions',

    "accounts.apps.AccountsConfig",
    "pages.apps.PagesConfig",
    "books.apps.BooksConfig",

    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
]

CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 604800
CACHE_MIDDLEWARE_KEY_PREFIX = ""

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.request',
            ],
        },
    },
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # Needed to log in by username in Django admin, regardless of 'allauth'
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth' specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'sana451@mail.ru'
EMAIL_HOST_PASSWORD = env("MAIL_RU_APP_PASSWORD")

# DEFAULT_FROM_EMAIL = "admin@djangobookstore.com"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

WSGI_APPLICATION = 'django_project.wsgi.application'

DATABASES = {
    "default": env.dj_db_url("DATABASE_URL", default="postgres://postgres@db/postgres")
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "accounts.CustomUser"

LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT = "home"
ACCOUNT_SESSION_REMEMBER = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_EMAIL_VERIFICATION = "none"

# django-crispy-forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

SOCIALACCOUNT_PROVIDERS = {
    "github": {
        "django_for_professionals": {
            "client_id": env("DJANGO_GITHUB_CLIENT_ID"),
            "secret": env("DJANGO_GITHUB_SECRET"),
        }
    }
}

INTERNAL_IPS = [
    "127.0.0.1",
]

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]

SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=False)
SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=0)
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=False)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=False)
CSRF_COOKIE_SECURE = env.bool("DJANGO_CSRF_COOKIE_SECURE", default=False)
SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE", default=False)
