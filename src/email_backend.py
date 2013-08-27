#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.mail.backends.smtp import EmailBackend
from django.conf import settings
from django.core.mail.message import sanitize_address
from django.core.exceptions import ImproperlyConfigured
from django.utils.encoding import force_bytes


def admin_emails():
    emails = set()
    for item in settings.ADMINS + settings.MANAGERS:
        if isinstance(item, (list, tuple)):
            emails.add(item[-1])
        else:
            emails.add(item)
    return emails


class DevEmailBackend(EmailBackend):

    def _send(self, email_message):
        """A helper method that does the actual sending."""
        if not email_message.recipients():
            return False

        if set(email_message.recipients()).issubset(admin_emails()):
            # Skip on admin notifications
            return super(DevEmailBackend, self)._send(email_message)

        from_email = sanitize_address(email_message.from_email, email_message.encoding)
        try:
            recipients = [sanitize_address(addr, email_message.encoding)
                          for addr in settings.DEV_EMAIL_LIST]
        except:
            raise ImproperlyConfigured("You must set a DEV_EMAIL_LIST setting to use the Dev Email Backend.")

        message = email_message.message()
        charset = message.get_charset().get_output_charset() if message.get_charset() else "utf-8"
        try:
            self.connection.sendmail(from_email, recipients,
                                     force_bytes(message.as_string(), charset))
        except:
            if not self.fail_silently:
                raise
            return False
        return True
