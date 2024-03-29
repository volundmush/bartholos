from django.conf.global_settings import *

del DEFAULT_FILE_STORAGE
del STATICFILES_STORAGE

import os as _os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": _os.path.join("data", "server.sqlite3"),
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

INSTALLED_APPS.extend(
    [
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.admindocs",
        "django.contrib.flatpages",
        "django.contrib.sites",
        "django.contrib.staticfiles",
        "bartholos.db.idmapper",
        "bartholos.db.autoproxy",
        "bartholos.db.objects",
        "bartholos.db.properties",
        "bartholos.db.users",
        "bartholos.db.players",
    ]
)

AUTH_USER_MODEL = "users.UserDB"
