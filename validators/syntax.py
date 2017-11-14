import re

from .base import EmailAddressValidator

VALID_EMAIL_RE = re.compile(
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"'  # quoted-string
    r')@(?:[A-Z0-9]+(?:-*[A-Z0-9]+)*\.)+[A-Z]{2,6}$', re.IGNORECASE)


class SyntaxValidator(EmailAddressValidator):

    def validate(self, email):
        if not email:
            return False
        m = VALID_EMAIL_RE.match(email)
        if m is None:
            raise ValueError('Invalid syntax')
        return True
