import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# ======================
# SECURITY
# ======================

SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-secret-key")

# In backend/settings.py
ALLOWED_HOSTS = [
    "jarrurat-care-app.onrender.com",
    ".onrender.com",  # This allows ALL Render domains
    "localhost",
    "127.0.0.1", 
]

# For now, keep DEBUG True to see errors
DEBUG = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# ======================
# APPLICATIONS
# ======================
# Static files for production
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "volunteers",
    "chatbot",
]


# ======================
# MIDDLEWARE
# ======================

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ======================
# TEMPLATES  ✅ (THIS WAS MISSING → CAUSED 500 ERROR)
# ======================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]



# ======================
# CORS / CSRF
# ======================

CORS_ALLOWED_ORIGINS = [
    "https://jarrurat-care-app.netlify.app",
]

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    "https://jarrurat-care-app.netlify.app",
    "https://jarrurat-care-app.onrender.com",
]

# ======================
# URLS / WSGI
# ======================

ROOT_URLCONF = "backend.urls"
WSGI_APPLICATION = "backend.wsgi.application"

# ======================
# DATABASE
# ======================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ======================
# I18N
# ======================

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# ======================
# DEFAULT PK
# ======================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ======================
# JAZZMIN
# ======================

JAZZMIN_SETTINGS = {
    "site_title": "Jarrurat Care Admin",
    "site_header": "Jarrurat Care Dashboard",
    "site_brand": "Jarrurat Care",
    "welcome_sign": "Welcome to Admin Panel",

    "topmenu_links": [
        {
            "name": "Frontend",
            "url": "https://jarrurat-care-app.netlify.app",
            "new_window": True,
        },
    ],

    "theme": "darkly",
}
