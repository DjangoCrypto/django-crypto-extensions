.. _usage:

Usage
=====

Django Models CryptoField Package
---------------------------------------
A set of generic common Djano Fields that automatically encrypt data for database amd encrypt for the purpose of usage in Django:

+ ``CryptoFieldMixin`` - Mixin that implement encrypt/decrypt methods.

Example of how to use to create custom CryptoTextField::

        # models.py

        from django.db import models

        from django_crypto_extensions.django_fields import *

        class CustomCryptoTextField(CryptoFieldMixin, models.TextField):
            pass

+ ``CryptoTextField`` - TextField inheriting Field
+ ``CryptoCharField`` - CharField inheriting Field
+ ``CryptoEmailField`` - EmailField inheriting Field
+ ``CryptoIntegerField`` - IntegerField inheriting Field
+ ``CryptoDateField`` - DateField inheriting Field
+ ``CryptoDateTimeField`` - DateTimeField inheriting Field
+ ``CryptoBigIntegerField`` - BigIntegerField inheriting Field
+ ``CryptoPositiveIntegerField`` - PositiveIntegerField inheriting Field
+ ``CryptoPositiveSmallIntegerField`` - PositiveSmallIntegerField inheriting Field
+ ``CryptoSmallIntegerField`` - SmallIntegerField inheriting Field

**Settings**

+ each CryptoField has 2 kwargs ``salt_settings_env`` and ``password``.
+ salt_settings_env - name of variable stored in ``settings.py`` file, which will be used as cryptographic salt. ``default: salt_settings_env = 'SECRET_KEY'`` if settings not set or no SECRET_KEY in setting ``default: salt = "Salt123!!!"``
+ password - password to be used in encryption process of given field (together with salt set globally) ``default = 'password'``
+ password_field - name of field from which to import password. It i most recommended to ue @property instead of actual field

**Example**::

    # models.py

    from django.db import models

    from django_crypto_extensions.django_fields import CryptoEmailField

    class TestCryptoEmail(models.Model):

        value = CryptoEmailField(salt_settings_env='NEW_SECRET_KEY', password='new_password')


**Example2**::

    # models.py

    from django.db import models

    from django_crypto_extensions.django_fields import CryptoEmailField

    class CryptoTextModelPasswordFromField(models.Model):

        @property
        def password(self):
            return "password_field_to_be_used_as_key"

        value = CryptoTextField(password_field="password")

CryptoBinaryField and CryptoCharField
---------------------------------------

+ A django-rest-framework fields for handling encryption through serialisation. Inputs are String object and internal python representation is Binary object for CryptoBinaryField and String object for CryptoCharField

+ It takes the optional parameter ``salt`` (Django SECRET_KEY imported from setting as default). If set it use custom cryptographic salt
+ It takes the optional parameter ``password`` ("Non_nobis1solum?nati!sumus" as default). If set it use a custom password in encryption. **It is highly recommended to use custom one!!**
+ It takes the optional parameter ``ttl`` (None as default). If set it manage the number of seconds old a message may be for it to be valid. If the message is older than ttl seconds (from the time it was originally created) field will return None and encrypted message will not be enabled for decryption.

**Example**::

    from rest_framework import serializers
    from drf_extra_fields.crypto_fields import CryptoCharField


    class CryptoSerializer(serializers.Serializer):
      crypto_char = CryptoCharField()

**Example with parameters**
+ It takes custom salt and password. Once saved it will be available for decryption for 1000 seconds.::

    from rest_framework import serializers
    from drf_extra_fields.crypto_fields import CryptoCharField


    class CryptoSerializer(serializers.Serializer):
    crypto_char = CryptoCharField(salt="custom salt", password="custom password", ttl=1000)

