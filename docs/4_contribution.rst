.. _contribution:


CONTRIBUTION
=================

**TESTS**

Make sure that you add the test for contributed field to ``test/*.py`` and run with command before sending a ``pull request``::

    $ pip install tox  # if not already installed
    $ tox

Or, if you prefer using Docker (recommended)::

    docker build -t django_crypto_extensions .
    docker run -v $(pwd):/app -it django_crypto_extensions /bin/bash
    tox
