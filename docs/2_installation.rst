.. _installation:

Installation
============

Django Crypto Extensions is easy to install from the PyPI package::

    $ pip install django-crypto-extensions

After installing the package, the project settings need to be configured.

**1.** Add ``django_crypto_extensions`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Django Crypto Extensions app can be in any position in the INSTALLED_APPS list.
        'django_crypto_extensions',
    ]


