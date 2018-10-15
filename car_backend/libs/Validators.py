# -*- coding: utf-8 -*-

import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_phone(value):
    if not re.match(r'”1[1-9]\\d{4}(\\d)\\1{4}"',value):
        raise ValidationError(_('%(value)不是一个有效手机号'), params={'value': value}, )