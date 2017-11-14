"""
Needs package python3-dns
"""

import DNS
import time

from .base import EmailAddressValidator


def get_mxrecords(domain):
    request = DNS.Request()
    reply = request.req(name=domain, qtype=DNS.Type.MX)
    return reply and reply.answers or []


def get_mxrecords_dummy(domain):
    time.sleep(.5)
    return []


class HostValidator(EmailAddressValidator):

    def validate(self, email):
        domain = email.split('@')[1]
        mxrecords = get_mxrecords_dummy(domain)
        if len(mxrecords) == 0:
            raise ValueError('Cannot find MX records for {}'.format(domain))
        return True
