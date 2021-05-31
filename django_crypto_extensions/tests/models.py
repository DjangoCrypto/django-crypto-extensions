# -*- coding: utf-8 -*-
from django.db import models

from django_crypto_extensions.django_fields import (
    CryptoTextField,
    CryptoCharField,
    CryptoEmailField,
    CryptoIntegerField,
    CryptoDateField,
    CryptoDateTimeField,
    CryptoBigIntegerField,
    CryptoPositiveIntegerField,
    CryptoPositiveSmallIntegerField,
    CryptoSmallIntegerField,
)


class CryptoTextModel(models.Model):
    text_field = CryptoTextField()


class CryptoTextModelPassword(models.Model):
    # text_field = CryptoTextField(password="password_to_be_used_as_key")
    text_field = CryptoTextField(password="password_to_be_used_as_key")


class CryptoTextModelPasswordFromField(models.Model):

    @property
    def password(self):
        return "password_field_to_be_used_as_key"

    # text_field = CryptoTextField(password_settings="SECRET_KEY")
    text_field = CryptoTextField(password_field="password")
    text_field2 = CryptoTextField(password="password_field_to_be_used_as_key")


class CryptoAllFieldModel(models.Model):
    text_field = CryptoTextField()
    char_field = CryptoCharField(max_length=10)
    email_field = CryptoEmailField()
    int_field = CryptoIntegerField()
    date_field = CryptoDateField()
    date_time_field = CryptoDateTimeField()
    big_int_field = CryptoBigIntegerField()
    positive_int_field = CryptoPositiveIntegerField()
    positive_small_int_field = CryptoPositiveSmallIntegerField()
    small_int_field = CryptoSmallIntegerField()
