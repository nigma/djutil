#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.timezone import now as tznow, localtime


def format_hour(t):
    v = t.strftime("%H:%M")
    if v[0] == "0":
        return v[1:]
    return v


def get_local_time():
    return localtime(tznow())


def get_local_date():
    return get_local_time().date()
