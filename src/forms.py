#-*- coding: utf-8 -*-

from __future__ import unicode_literals

import crispy_forms.helper


class DefaultFormHelper(crispy_forms.helper.FormHelper):
    def __init__(self, form=None):
        super(DefaultFormHelper, self).__init__(form=form)
        self.form_class = "form-horizontal"
        self.html5_required = True
        self.help_text_inline = True
