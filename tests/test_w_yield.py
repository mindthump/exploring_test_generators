from util import simple_wrapper, retry, forgiving_wrapper
from test_base import TestBase
from nose.tools import assert_equals, assert_true, nottest
from nose.plugins.attrib import attr
from nose.plugins.skip import SkipTest
import nose
import inspect
import logging
from twiddle import Twiddle

logger = logging.getLogger(__name__)


def setup_module():
    logger.debug("Module setup_module: pull the lever ##########################")


def teardown_module():
    logger.debug("Module teardown_module: push the lever ##########################")


class TestTwiddling(TestBase):
    @classmethod
    def setup_class(cls):
        logger.debug("Class setup_class: tie the knot ==========================")


    @classmethod
    def teardown_class(cls):
        logger.debug("Class teardown_class: untie the knot ==========================")


    def setup(self):
        logger.debug("Method setup: lift the lid --------------------------")


    def teardown(self):
        logger.debug("Method teardown: drop the lid --------------------------")


    @attr('twiddletest')
    @attr('weekly')
    @attr(versions='all')
    @attr(status='wip')
    def test_twiddling_all(self):
        """
        NOTE: This is the _test_generator_ of multiple tests
        Test twiddling every version, one at a time
        ("version" is a placeholder for whatever parameters are needed)
        """
        logger.info(">>Test Start: %s" % inspect.stack()[0][3])

        versions = ["Able", "Baker", "Charlie", "Dog", "Easy", "Fox", ]
        platforms = ["Macintosh", "Linux"]

        for version in versions:
            for platform in platforms:
                test_desc = "Testing twiddling of version = '{}' platform = '{}'".format(version, platform)
                # Nose uses this value in the results output, otherwise it just uses the vanilla docstring over and over
                self.verify_twiddle.__func__.description = test_desc
                logger.info(test_desc)
                yield self.verify_twiddle, version, platform

        logger.info("<<Test Complete: %s" % inspect.stack()[0][3])


    @retry(retries=3, wait=2, patience=2)
    def verify_twiddle(self, version, platform):
        """
        NOTE: This is the _test_ which exercises the function itself
        The retry is handled by the @retry decorator
        :param version:
        :return:
        """
        # TODO: The generator might be able to call straight to the FUT without this intermediate
        # or this could include other specialized functionality -- perhaps more logging or
        # something in a try/catch if the retries are exhausted vs. other exceptions?
        self.verify_twiddle.__func__.description = ""
        Twiddle().twiddle(version, platform)


class TestBar(TestBase):
    @attr(status='good')
    def test_base_fixtures(self):
        logger.debug("++++ In the TestBar class, this is to see if the base class fixtures run")

    @attr(status='good')
    @forgiving_wrapper
    def test_forgiving_wrapper(self):
        logger.debug("++++ Do some cool crap here")
        assert False, "Did a bad thing, but we're in a forgiving wrapper"

    @attr('daily')
    @attr(versions='latest')
    @attr(status='bad')
    def test_reality(self):
        logger.info("++++ Reality Test: nothing unreal exists")
        try:
            assert_equals("real", "rael")
        except AssertionError as ae:
            logger.info('Ha! The test_reality assertion failure gets swallowed by an except clause.')

