# coding=utf-8
"""
A minimal module to demonstrate test generators.
"""
from random import randint
import logging

logger = logging.getLogger(__name__)


class Twiddle(object):
    """
    The object to be tested.
    """

    def __init__(self, version, platform):
        """Create a new Twiddle"""
        self.version = version
        self.platform = platform

    def twiddle(self):
        """
        This is the function itself, it fails 1/3 of the time
        Assume this function can't be touched
        :return:
        """
        outcome = randint(0, 2)
        logger.info(
            "Twiddling, version = '{}' platform = '{}'".format(
                self.version, self.platform
            )
        )
        if outcome == 0:
            raise TwiddleSpecialException("Twiddle failure!")


class TwiddleSpecialException(Exception):
    """
    Custom exception for twiddle() failures.
    """

    pass
