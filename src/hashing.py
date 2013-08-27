#-*- coding: utf-8 -*-

from __future__ import unicode_literals

import hashlib
import os
import random

from django.db import models
from django.utils import six
from django.utils.encoding import force_str
from django.utils.timezone import now as tznow


def generate_hash(string, salt=None):
    if salt is None:
        salt = hashlib.sha1(force_str(random.random())).hexdigest()[:5]
    hash = hashlib.sha1(force_str(salt) + force_str(string)).hexdigest()
    return salt, hash


def make_upload_to(base_path, by_fk_field=None):
    """
    Creates ``upload_to`` function that generates hashed paths
    for file uploads.

    Filename hash is created from instance.pk and current time.
    
    Generated paths consist of:

    {base_path}/{optional related field id/value hash}/{hashed filename}.{ext}

    :param base_path: Base path for upload
    :type base_path: str or unicode
    :type by_fk_field: str or unicode
    :param by_fk_field: Optional field name of related (parent) object.
                            Its pk hash will be part of a generated path.
    """

    if not base_path.endswith("/"):
        base_path += "/"

    def get_field_value(field):
        if isinstance(field, six.string_types + (int,)):
            return field
        elif isinstance(field, models.Model):
            value = field.pk
            assert value
            return value

    def upload_to(instance, filename):
        """
        Returns upload path for FileField

        :type instance: :class:`django.db.models.Model`
        :param str filename:
        :rtype: str
        """
        extension = os.path.splitext(filename)[-1].lower()
        salt, hash_instance = generate_hash(instance.pk)
        salt, hash_time = generate_hash(tznow().isoformat())

        fk_subdir = ""
        if by_fk_field:
            fk_field = getattr(instance, by_fk_field)
            fk_value = get_field_value(fk_field)
            salt, hash_fk = generate_hash(force_str(fk_value), salt="")
            fk_subdir = "{hash}/".format(hash=hash_fk[:6])

        return "{path}{fk_subdir}{hash}{extension}".format(
            path=base_path,
            fk_subdir=fk_subdir,
            hash=hash_instance[:10] + hash_time[:6],
            extension=extension
        )
    return upload_to
