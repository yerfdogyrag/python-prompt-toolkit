"""
"""
from __future__ import unicode_literals
from abc import ABCMeta, abstractmethod
from six import with_metaclass

__all__ = (
    'ValidationError',
)


class ValidationError(Exception):
    def __init__(self, index=0, message=''):
        super(ValidationError, self).__init__(message)
        self.index = index

    def __repr__(self):
        return '%s(index=%r, message=%r)' % (
            self.__class__.__name__, self.index, self.message)


class Validator(with_metaclass(ABCMeta, object)):
    @abstractmethod
    def validate(self, document):
        """
        Validate the input.
        If invalid, this should raise `self.validation_error`.
        """
        pass
