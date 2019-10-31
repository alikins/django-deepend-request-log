django-deepend-request-log
==========================

Plug django-request-logging into your Django project and you will have intuitive and color coded request/response payload logging, for both web requests and API requests. Supports Django 1.8+.

## Installing

```bash
$ pip install django-deepend-request-log
```

Then add ```deependrequestlog.middleware.LogRequestMiddleware``` to your ```MIDDLEWARE```.

For example:

```python
MIDDLEWARE = (
    ...,
    'deependrequestlog.middleware.LogRequestMiddleware',
    ...,
)
```

And configure logging in your app:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
```
