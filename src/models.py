#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampedModel(models.Model):

    created_at      = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_at     = models.DateTimeField(_("Modified at"), auto_now=True)

    class Meta:
        abstract = True


class AuthorTimeStampedModel(models.Model):

    created_by      = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Created by"),
                        null=True, blank=True, on_delete=models.SET_NULL, editable=False, related_name="+")
    created_at      = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_at     = models.DateTimeField(_("Modified at"), auto_now=True)

    class Meta:
        abstract = True


def get_or_none(qs, *args, **kwargs):
    try:
        return qs.get(*args, **kwargs)
    except models.ObjectDoesNotExist:
        return None
