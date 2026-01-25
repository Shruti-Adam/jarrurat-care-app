import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ==============================
# SECURITY SETTINGS
# ==============================

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-fallback-key")

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "jarrurat-care-app.onrender.com",
]

# Required for Render HTTPS
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# ==============================
# APPLICATION DEFINITION
# ==============================

INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',

    'volunteers',
    'chatbot',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # MUST be here
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==============================
# CORS & CSRF (REACT + NETLIFY)
# ==============================

CORS_ALLOWED_ORIGINS = [
    "https://jarrurat-care-app.netlify.app",
]

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    "https://jarrurat-care-app.netlify.app",
    "https://jarrurat-care-app.onrender.com",
]

# ==============================
# URLS / WSGI
# ==============================

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

# ==============================
# DATABASE (SQLite – OK for now)
# ==============================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ==============================
# PASSWORD VALIDATION
# ==============================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==============================
# INTERNATIONALIZATION
# ==============================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ==============================
# STATIC FILES (RENDER)
# ==============================


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Add this for production on Render
if 'RENDER' in os.environ:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# ==============================
# DEFAULT PRIMARY KEY
# ==============================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==============================
# JAZZMIN SETTINGS
# ==============================

JAZZMIN_SETTINGS = {
    "site_title": "LearnSphere Admin",
    "site_header": "LearnSphere Dashboard",
    "site_brand": "LearnSphere",
    "welcome_sign": "Welcome to LearnSphere Admin",

    # IMPORTANT: point to Netlify frontend
    "topmenu_links": [
        {
            "name": "Frontend",
            "url": "https://jarrurat-care-app.netlify.app",
            "new_window": True
        },
    ],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },

    "theme": "darkly",
}
