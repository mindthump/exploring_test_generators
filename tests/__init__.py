from __future__ import print_function

import logging

logger = logging.getLogger('tests')


def setup_package():
    logger.debug("Package __init__ setup_package: Open the door")


def teardown_package():
    logger.debug("Package __init__ teardown_package: Close the door")
