import logging

logger = logging.getLogger(__name__)


class TestBase(object):
    """
    Base Test Object
        These can be overidden in subclasses
    """

    @classmethod
    def setup_class(cls):
        logger.info(">> Base Class default setup_class: tie the knot")

    @classmethod
    def teardown_class(cls):
        logger.info("<< Base Class default teardown_class: untie the knot")

    def __init__(self):
        pass

    def setup(self):
        logger.info(">>> TestBase default method setup: turn on the lights")

    def teardown(self):
        logger.info("<<< TestBase default method teardown: turn off the lights")
