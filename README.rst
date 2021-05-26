DJANGO-CRYPTO-EXTENSIONS
========================


.. image:: https://img.shields.io/pypi/v/django-crypto-extensions
    :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/django-crypto-extensions
    :alt: PyPI - Python Version

.. image:: https://readthedocs.org/projects/django-crypto-extensions/badge/?version=latest
   :target: https://django-crypto-extensions.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation

.. image:: https://travis-ci.com/DjangoCrypto/django-crypto-extensions.svg?branch=main
    :target: https://travis-ci.com/DjangoCrypto/django-crypto-extensions
    :alt: Travis CI


Documentation
-------------

For more information on installation and configuration see the documentation at:

https://django-crypto-extensions.readthedocs.io/


CONTRIBUTION
=================

**TESTS**

- Make sure that you add the test for contributed field to test/test_fields.py and run with command before sending a
  pull request:

```bash
$ pip install tox  # if not already installed
$ tox
```

Or, if you prefer using Docker (recommended):

```bash
docker build -t django_crypto_extensions .
docker run -v $(pwd):/app -it django_crypto_extensions /bin/bash
tox
```
