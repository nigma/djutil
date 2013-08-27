#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import messages


class ActionMessageMixin(object):
    """
    Augments `form edit` and `object delete` actions and provides easy way
    to display and define success messages using message dict.
    """
    messages = None
    success_message_key = None

    def get_success_message(self, success_message_key=None):
        if self.messages:
            key = success_message_key if success_message_key else self.success_message_key
            if key in self.messages:
                return self.messages[key]

    def add_message(self, success_message_key=None):
        message = self.get_success_message(success_message_key)
        if message:
            messages.add_message(self.request, **message)

    def form_valid(self, form):
        response = super(ActionMessageMixin, self).form_valid(form)
        self.add_message()
        return response

    def delete(self, request, *args, **kwargs):
        response = super(ActionMessageMixin, self).delete(request, *args, **kwargs)
        self.add_message()
        return response
