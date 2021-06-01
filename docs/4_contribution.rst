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


Publishing new releases
========================

Increment version in ``django_crypto_extensions/__init__.py``. For example::

    __version__ = '0.2.2'  # from 0.2.1

Move to new version section all release notes in documentation.

Add date for release note section.

Replace in documentation all ``New in Django Crypto Extensions development version`` notes to ``New in Django Crypto Extensions 0.2.2``.

Rebuild documentation.

Run tests.

Commit changes with message "Version 0.2.2"

Add new tag version for commit:

    $ git tag 0.2.2

Push to master with tags:

    $ git push origin main --tags

Don't forget to merge `master` to `gh-pages` branch and push to origin:

    $ git co gh-pages
    $ git merge --no-ff master
    $ git push origin gh-pages

Publish to pypi:

    $ python setup.py publish