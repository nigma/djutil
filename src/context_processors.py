#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.utils import dateformat


def analytics(request):
    return {
        "ga_tracking_id": getattr(settings, "GA_TRACKING_ID", ""),
        "ga_tracking_domain": getattr(settings, "GA_TRACKING_DOMAIN", "")
    }


def version_string(request):
    revision_hash = getattr(settings, "REVISION_HASH", "")
    revision_date = getattr(settings, "REVISION_DATE", "")

    if revision_date:
        try:
            revision_date = dateformat.format(revision_date, "j M, G:i")
        except:
            revision_date = ""

    revision_env = getattr(settings, "REVISION_ENV", "")
    if revision_env:
        revision_env = ", " + revision_env

    if revision_hash and revision_date:
        version = "v. {} ({}{})".format(revision_date, revision_hash, revision_env)
    else:
        version = ""

    return {"VERSION_STRING": version}
