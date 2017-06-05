DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dmp',
        'USER': 'dmp',
        'PASSWORD': 'fdir498djd4',
        'HOST': '127.0.0.1',
        'PORT': '',
        'OPTIONS'  : { 'init_command' : 'SET storage_engine=InnoDB', },
    },
}