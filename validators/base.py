from abc import abstractmethod


class PluginMount(type):

    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, 'plugins'):
            # we are processing the mount point itself
            cls.plugins = []
        else:
            cls.plugins.append(cls)


class EmailAddressValidator(metaclass=PluginMount):
    """
    validate(self, email):
            Recieves an email address to validate.
    """

    @classmethod
    def colname(cls):
        """Return the class name in a form suitable for a column header"""
        return cls.__name__.replace('Validator', '')

    def validate(self, email):
        """Validate email address. Return true if valid, or false otherwise"""

    def is_valid(self, email):
        """Implement a check in terms of the class validate method."""
        try:
            return self.validate(email)
        except ValueError:
            return False
