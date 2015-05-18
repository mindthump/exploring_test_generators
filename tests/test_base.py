import logging

logger = logging.getLogger(__name__)

### These fixtures both get executed before anything but the package_setup fixture
# def setup_module():
#     logger.debug("TestBase Module (default) setup_module: pull the lever B####B####B####B####B####B")
#
# def teardown_module():
#     logger.debug("TestBase Module (default) teardown_module: push the lever B####B####B####B####B####B")


class TestBase(object):
    """
    Base Test Object
    """

    @classmethod
    def setup_class(cls):
        logger.debug("TestBase Class (default) setup_class: tie the knot B====B====B====B====B====B")

    @classmethod
    def teardown_class(cls):
        logger.debug("TestBase Class (default) teardown_class: untie the knot B====B====B====B====B====B")


    def __init__(self):
        pass


    def setup(self):
        """
        These can be overidden in subclasses
        :return:
        """
        logger.debug("TestBase Method (default) setup: turn on the lights B----B----B----B----B----B")

    def teardown(self):
        logger.debug("TestBase Method (default) teardown: turn off the lights B----B----B----B----B----B")