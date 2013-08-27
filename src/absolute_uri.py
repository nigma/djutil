#-*- coding: utf-8 -*-

from __future__ import unicode_literals

import urlparse

from django.contrib.sites.models import get_current_site


def add_domain(path, domain, secure=False):
    if path.startswith("http://") or path.startswith("https://"):
        return path
    domain = ("https://" if secure else "http://") + domain
    return urlparse.urljoin(domain, path)


def build_site_url(path, request=None):
    current_site = get_current_site(request=request)
    domain = current_site.domain
    secure = request.is_secure() if request is not None else False
    return add_domain(path, domain, secure=secure)
