#local_settings file
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'eci',
        'USER': 'eci_athul',
        'PASSWORD': 'eci_athul',
        'HOST': 'localhost',
        'PORT': '',
    }
}