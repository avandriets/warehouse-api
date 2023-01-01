from pathlib import Path
from dotenv import load_dotenv
import os
from pathlib import Path
from datetime import timedelta

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = int(os.environ.get('DEBUG', default=0))
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(' ')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',  # Great packaged to access abstract models
    'django_filters',  # Used with DRF
    'rest_framework',  # DRF package
    'rest_framework.authtoken',
    'drf_spectacular',
    'core',
    'user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'warehouse.middleware.KeycloakMiddleware'
]

ROOT_URLCONF = 'warehouse.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'warehouse.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'core.User'

REST_FRAMEWORK = {
    # 'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    # 'DEFAULT_PARSER_CLASSES': (
    #     'rest_framework_json_api.parsers.JSONParser',
    # ),
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework_json_api.renderers.JSONRenderer',
    #     'rest_framework.renderers.BrowsableAPIRenderer'
    # ),
    # 'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
    # 'DEFAULT_FILTER_BACKENDS': (
    #     'rest_framework_json_api.filters.QueryParameterValidationFilter',
    #     'rest_framework_json_api.filters.OrderingFilter',
    #     'rest_framework_json_api.django_filters.DjangoFilterBackend',
    #     'rest_framework.filters.SearchFilter',
    # ),
    # 'SEARCH_PARAM': 'filter[search]',
    # 'TEST_REQUEST_RENDERER_CLASSES': (
    #     'rest_framework_json_api.renderers.JSONRenderer',
    # ),
    # 'TEST_REQUEST_DEFAULT_FORMAT': 'vnd.api+json',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    # 'DEFAULT_PERMISSION_CLASSES': 'rest_framework.permissions.IsAuthenticated',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'user.user_backend.MyBackend',
        # 'rest_framework_simplejwt.authentication.JWTStatelessUserAuthentication'
    ],
}

SPECTACULAR_SETTINGS = {
    'COMPONENT_SPLIT_REQUEST': True,
}

KEYCLOAK_BEARER_AUTHENTICATION_EXEMPT_PATHS = [
    'admin', 'account',
]

CONFIG_DIR = os.path.join(os.path.dirname(__file__), os.pardir)

KEYCLOAK_CLIENT_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsGdXrKR1KxXw0O7ldV5lF7ZTfqRKoX4A+rVA8iJkAhn35zWx3PsPNXVAGTV90vEoAJp3YroUHj7sNq2opXm8HcUJyxLGtpkBJ4ECA+ql1uUjdz/Nw+cZFEW78cdurOPET/WxmWzASAR7FhZMDGYMJ3mQb3CT6GXfK78XTlKua+f83u0cSEoAhBYjSgLpbO7kvGHDuxBVCOV2/RQAK4k+LIdMpgA4uk+idSa1qnVgmWgZwHungxspUzrXrE5G7VN0w8nDQ1DEL75JKVB+IBoXcqa7+BTUn/9Nbs4QTJ2F75jjo/rTwYk+jUx2FQpNlzQpGfccJ57b5ff++yIm2JAaeQIDAQAB
-----END PUBLIC KEY-----"""

KEYCLOAK_CONFIG = {
    'KEYCLOAK_REALM': 'master',
    'KEYCLOAK_CLIENT_ID': 'warehouse',
    'KEYCLOAK_DEFAULT_ACCESS': 'ALLOW',  # DENY or ALLOW
    'KEYCLOAK_AUTHORIZATION_CONFIG': os.path.join(CONFIG_DIR, 'warehouse.json'),
    'KEYCLOAK_METHOD_VALIDATE_TOKEN': 'DECODE',
    'KEYCLOAK_SERVER_URL': 'http://127.0.0.1:18080/auth/',
    'KEYCLOAK_CLIENT_SECRET_KEY': '9OeN-hiqwN23su1zhMmW8VCt4rhLqL1CRuo1xYD2cnU',
    'KEYCLOAK_CLIENT_PUBLIC_KEY': KEYCLOAK_CLIENT_PUBLIC_KEY,
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ALGORITHM': 'RS256',
    'SIGNING_KEY': SECRET_KEY,
    # 'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('JWT',),
    # 'USER_ID_FIELD': 'id',
    # 'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    # 'TOKEN_TYPE_CLAIM': 'token_type',
}
