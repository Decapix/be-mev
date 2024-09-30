"""
ok thi is the right file
"""

from pathlib import Path
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!


DEBUG = True


ALLOWED_HOSTS = ['be-mev-e942436feae3.herokuapp.com', '127.0.0.1', 'be-mev.herokuapp.com', 'be-mev.com', 'www.be-mev.com', 'be-mev.fr', 'www.be-mev.fr']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    'storages',
    "django.contrib.messages",
    'django.contrib.staticfiles',
    'django.contrib.sites',  

    'constance.backends.database',
    'constance',
    'widget_tweaks',

    'faq',
    'client',
    'super',
    'client_form'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

]

ROOT_URLCONF = "mevsite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "mevsite.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'madb',
        'USER': 'postgres',
        'PASSWORD': ':)Solenops1s<$o',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOCALE_PATHS = (
    BASE_DIR / 'locale', 
)

if os.environ.get('ENV') == "PRODUCTION":
    db_from_env = dj_database_url.config(conn_max_age=600)
    DATABASES['default'].update(db_from_env)
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    STATIC_ROOT = BASE_DIR / 'staticfiles'

    MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / "media"



STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']


SITE_ID = 1


API_GOOGLE = os.environ.get('API_GOOGLE')

# Configuration pour utiliser SSL/TLS avec Heroku et Cloudflare (https)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# email



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_FROM = 'mev.message@gmail.com'
EMAIL_HOST_USER = 'mev.message@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True


BOARD_ID = os.environ.get('BOARD_ID')
KEY_TRELLO = os.environ.get('KEY_TRELLO')
TOKEN_TRELLO = os.environ.get('TOKEN_TRELLO')

ID_LIST_1 = os.environ.get('ID_LIST_1')
ID_LIST_2 = os.environ.get('ID_LIST_2')
ID_LIST_3 = os.environ.get('ID_LIST_3')
ID_LIST_4 = os.environ.get('ID_LIST_4')
ID_LIST_5 = os.environ.get('ID_LIST_5')
ID_LIST_6 = os.environ.get('ID_LIST_6')



# constance

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {
    'aide_individuel-Bleu1': ('23541', 'aide_individuel-Bleu1'),
    'aide_individuel-Bleu2': ('34551', 'aide_individuel-Bleu2'),
    'aide_individuel-Bleu3': ('41493', 'aide_individuel-Bleu3'),
    'aide_individuel-Bleu4': ('48447', 'aide_individuel-Bleu4'),
    'aide_individuel-Bleu5': ('55427', 'aide_individuel-Bleu5'),
    'aide_individuel-Jaune2': ('42058', 'aide_individuel-Jaune2'),
    'aide_individuel-Jaune3': ('50513', 'aide_individuel-Jaune3'),
    'aide_individuel-Jaune4': ('58981', 'aide_individuel-Jaune4'),
    'aide_individuel-Jaune5': ('67473', 'aide_individuel-Jaune5'),
    'aide_individuel-Jaune+': ('8486', 'aide_individuel-Jaune+'),
    'aide_individuel-Violet1': ('40018', 'aide_individuel-Violet1'),
    'aide_individuel-Violet2': ('58827', 'aide_individuel-Violet2'),
    'aide_individuel-Violet3': ('70382', 'aide_individuel-Violet3'),
    'aide_individuel-Violet4': ('82839', 'aide_individuel-Violet4'),
    'aide_individuel-Violet5': ('94844', 'aide_individuel-Violet5'),
    'aide_individuel-Violet+': ('12006', 'aide_individuel-Violet+'),
    'aide_individuel-Rose1': ('40018', 'aide_individuel-Rose1'),
    'aide_individuel-Rose2': ('58827', 'aide_individuel-Rose2'),
    'aide_individuel-Rose3': ('70382', 'aide_individuel-Rose3'),
    'aide_individuel-Rose4': ('82839', 'aide_individuel-Rose4'),
    'aide_individuel-Rose5': ('94844', 'aide_individuel-Rose5'),
    'aide_individuel-Rose+': ('12006', 'aide_individuel-Rose+'),
    
    "Identification_f_description":(" ", "Identification_f_description"),
    "DescriptifDuLogement_f_description":(" ", "DescriptifDuLogement_f_description"),
    "BATI_f_description":(" ", "BATI_f_description"),
    "ChauffageEauChaude_f_description":(" ", "ChauffageEauChaude_f_description"),
    "Ventilation_f_description":(" ", "Ventilation_f_description"),
    "FinancementAvecEcoptz_f_description":(" ", "FinancementAvecEcoptz_f_description"),
    "FinancementSansEcoptz_f_description":(" ", "FinancementSansEcoptz_f_description"),
    "SituationProfessionnelle_fp_description":(" ", "SituationProfessionnelle_fp_description"),
    "CompositionMenage_fp_description":(" ", "CompositionMenage_fp_description"),
    "ProprietairesOccupantsIntro_fp_description":(" ", "ProprietairesOccupantsIntro_fp_description"),
    "AidesIndividuelles_fp_description":(" ", "AidesIndividuelles_fp_description"),
    "AidesIndividuellesQuestionComplementaire_fp_description":(" ", "AidesIndividuellesQuestionComplementaire_fp_description"),
    "DocumentComplementaire_f_description":(" ", "DocumentComplementaire_f_description"),

    # constance client follow project
    "CL_T1":(" ", "client follow proj, 1 titre"),
    "CL_D1":(" ", "client follow proj, 1 description"),
    "CL_T2":(" ", "client follow proj, 2 titre"),
    "CL_D2":(" ", "client follow proj, 2 description"),
    "CL_T3":(" ", "client follow proj, 3 titre"),
    "CL_D3":(" ", "client follow proj, 3 description"),
    "CL_T4":(" ", "client follow proj, 4 titre"),
    "CL_D4":(" ", "client follow proj, 4 description"),
    "CL_T5":(" ", "client follow proj, 5 titre"),
    "CL_D5":(" ", "client follow proj, 5 description"),
    "CL_T6":(" ", "client follow proj, 6 titre"),
    "CL_D6":(" ", "client follow proj, 6 description"),
}


# use
# from constance import config
# print(config.MY_SETTING)

URL_QR = "https://be-mev.com/admin_form/init-formulaire/"




# =============================================================================

# Cloudcube storage

# =============================================================================

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


cloudcube_base_url = os.environ.get('CLOUDCUBE_URL')


AWS_S3_ENDPOINT_URL = cloudcube_base_url

AWS_ACCESS_KEY_ID = os.environ.get('CLOUDCUBE_ACCESS_KEY_ID')

AWS_SECRET_ACCESS_KEY = os.environ.get('CLOUDCUBE_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = "mev-bucket"

AWS_S3_REGION_NAME = 'fr-par'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_FILE_OVERWRITE = False
