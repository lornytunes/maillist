import DNS

from .base import EmailAddressValidator


def get_mxrecords(domain):
    request = DNS.Request()
    reply = request.req(name=domain, qtype=DNS.Type.MX)
    return reply and reply.answers or []


class HostValidator(EmailAddressValidator):
    """Checks whether or not the domain of an email address has a valid MX record."""

    def validate(self, email):
        domain = email.split('@')[1]
        mxrecords = get_mxrecords(domain)
        if len(mxrecords) == 0:
            raise ValueError('Cannot find MX records for {}'.format(domain))
        return True
