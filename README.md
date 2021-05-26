DJANGO-CRYPTO-EXTENSIONS
================

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
