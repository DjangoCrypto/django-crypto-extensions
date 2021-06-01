import pickle

try:
    from functools import cached_property as property_decorator
except ImportError:
    from builtins import property as property_decorator

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.checks import Error
from django.db import models
from django.utils.encoding import force_bytes

import base64

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

__all__ = [
    "CryptoFieldMixin",
    "CryptoTextField",
    "CryptoCharField",
    "CryptoEmailField",
    "CryptoIntegerField",
    "CryptoDateField",
    "CryptoDateTimeField",
    "CryptoBigIntegerField",
    "CryptoPositiveIntegerField",
    "CryptoPositiveSmallIntegerField",
    "CryptoSmallIntegerField",
]

DEFAULT_PASSWORD = "Non_nobis1solum?nati!sumus"
DEFAULT_SALT_ENV = "SECRET_KEY"


def to_bytes(_obj):
    if isinstance(_obj, bytes):
        return _obj
    elif isinstance(_obj, (bytearray, memoryview)):
        return force_bytes(_obj)
    else:
        return pickle.dumps(_obj)


class CryptoFieldMixin(models.Field):
    """
    A Mixin that can be ued to convert standard django model field to encrypted binary. Fields are fully encrypted in
    data base, but automatically readable in Django. Therefore there is no need for additional description of data,
    it will be handheld automatically.

    Cryptography protocol used in mixin: Fernet (symmetric encryption) provided by Cryptography (pyca/cryptography)
    """

    def __init__(self, salt_settings_env=DEFAULT_SALT_ENV, password=DEFAULT_PASSWORD, password_field=None, *args,
                 **kwargs):

        if salt_settings_env and not isinstance(salt_settings_env, str):
            raise ImproperlyConfigured("'salt_settings_env' must be a string")
        self.salt_settings_env = salt_settings_env

        if password_field and not isinstance(password_field, str):
            raise ImproperlyConfigured("'password_field' must be a string or int")

        self.password_field = password_field
        # if password_field:
        #     self.password_field = password_field
            # self.password = self.get_password_from_field()

        if password and not isinstance(password, (str, int)):
            raise ImproperlyConfigured("'password' must be a string or int")

        # if password and password_field:
        #     raise ImproperlyConfigured("'password' must remain empty if 'password_field' ha been set")

        # if password_field is None and password:
        # if password:
        self.password = password

        if kwargs.get("primary_key"):
            raise ImproperlyConfigured(
                f"{self.__class__.__name__} does not support primary_key=True."
            )
        if kwargs.get("unique"):
            raise ImproperlyConfigured(
                f"{self.__class__.__name__} does not support unique=True."
            )
        if kwargs.get("db_index"):
            raise ImproperlyConfigured(
                f"{self.__class__.__name__} does not support db_index=True."
            )
        kwargs["null"] = True  # should be nullable, in case data field is nullable.
        kwargs["blank"] = True

        self.get_salt()

        self._internal_type = "BinaryField"
        super().__init__(*args, **kwargs)

    # def has_default(self):
    #     """Always use the EncryptedFields default"""
    #     return self.model._meta.get_field(self.password_field).has_default()
    #
    # def get_default(self):
    #     """Always use EncryptedField's default."""
    #     return self.model._meta.get_field(self.password_field).get_default()

    def get_salt(self):
        try:
            self.salt = getattr(settings, self.salt_settings_env)
        except AttributeError:
            raise Error(
                f"salt_settings_env {self.salt_settings_env} is not set properly"
            )

    # def pre_save(self, model_instance, add):
    #     """Save the original_value."""
    #     if self.password_field:
    #         password_field = getattr(model_instance, self.password_field)
    #         setattr(model_instance, self.attname, password_field)
    #     else:
    #         pass
    #     return super(CryptoFieldMixin, self).pre_save(model_instance, add)



    def generate_password_key(self, password, salt):
        # password = b"password"
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=to_bytes(salt),
            iterations=100000,
        )

        key = base64.urlsafe_b64encode(kdf.derive(to_bytes(password)))
        return key

    @property_decorator
    def fernet_key(self):
        key = self.generate_password_key(self.password, self.salt)
        return Fernet(key)

    def encrypt(self, message):
        b_message = to_bytes(message)
        encrypted_message = self.fernet_key.encrypt(b_message)
        return encrypted_message

    def decrypt(self, encrypted_message):
        b_message = to_bytes(encrypted_message)
        decrypted_message = self.fernet_key.decrypt(b_message)
        return decrypted_message

    def get_internal_type(self):
        return self._internal_type

    def get_db_prep_value(self, value, connection, prepared=False):
        if self.empty_strings_allowed and value == bytes():
            value = ""
        value = super().get_db_prep_value(value, connection, prepared=False)
        if value is not None:
            if self.password_field:
                self.password = models._meta.get_field(self.password_field)
            encrypted_value = self.encrypt(value)
            return encrypted_value
            # return connection.Database.Binary(encrypted_value)

    # def get_password_from_field(self, model_instance, add):
    #     # return getattr(settings, self.password_settings)
    #     if self.password_field:
    #         self.password = model_instance._meta.get_field(self.password_field)
    #     pass
        # try:
        #     # return self.model._meta.get_field(self.password_field)
        #     return self.model._meta.get_field(self.password_settings)
        # except AttributeError:
        #     raise Error(
        #         f"password_field {self.password_settings} is not set properly"
        #     )

    # def pre_save(self, model_instance, add):
    #
    #     if self.password_field:
    #         self.password = model_instance._meta.get_field(self.password_field)
    #         # self.get_password_from_field(model_instance, add)
    #     return super(CryptoFieldMixin, self).pre_save(model_instance, add)
        # encrypted_value = self.encrypt(self.attname)
        # if self.empty_strings_allowed and encrypted_value == bytes():
        #     return ""
        # return encrypted_value

    def from_db_value(self, value, expression, connection):
        if value is not None:
            data = self.decrypt(value)
            return pickle.loads(data)

    @property_decorator
    def validators(self):
        # For IntegerField (and subclasses) we must pretend to be that
        # field type to get proper validators.
        self._internal_type = super().get_internal_type()
        try:
            return super().validators
        finally:
            self._internal_type = "BinaryField"

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # Only include kwarg if it's not the default (None)
        if self.salt_settings_env:
            kwargs["salt_settings_env"] = self.salt_settings_env
        # if self.password:
        #     kwargs["password"] = self.password
        return name, path, args, kwargs


class CryptoTextField(CryptoFieldMixin, models.TextField):
    pass


class CryptoCharField(CryptoFieldMixin, models.CharField):
    pass


class CryptoEmailField(CryptoFieldMixin, models.EmailField):
    pass


class CryptoIntegerField(CryptoFieldMixin, models.IntegerField):
    pass


class CryptoPositiveIntegerField(CryptoFieldMixin, models.PositiveIntegerField):
    pass


class CryptoPositiveSmallIntegerField(
    CryptoFieldMixin, models.PositiveSmallIntegerField
):
    pass


class CryptoSmallIntegerField(CryptoFieldMixin, models.SmallIntegerField):
    pass


class CryptoBigIntegerField(CryptoFieldMixin, models.BigIntegerField):
    pass


class CryptoDateField(CryptoFieldMixin, models.DateField):
    pass


class CryptoDateTimeField(CryptoFieldMixin, models.DateTimeField):
    pass
