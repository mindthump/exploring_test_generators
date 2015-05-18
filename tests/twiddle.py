from util import retry
from random import randint
import logging

logger = logging.getLogger(__name__)

class Twiddle(object):

    def twiddle(self, version, platform):
        """
        This is the function itself, it fails 1/3 of the time
        Assume this function can't be touched
        :param version:
        :return:
        """
        outcome = randint(0, 2)
        logger.info("Twiddling, version = '{}' platform = '{}'".format(version, platform))
        if outcome == 0:
            raise TwiddleSpecialException("Twiddle failure!")


class TwiddleSpecialException(Exception): pass