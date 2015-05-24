from functools import wraps
import math
from time import sleep

import logging

logger = logging.getLogger(__name__)


def simple_wrapper(test_func):
    @wraps(test_func)
    def a_wrapper(self, *args, **kwargs):
        logger.debug("Some MetaStuff: In the wrapper before: %s > > > > > > > > > > > > >" % args[0])
        test_func(self, *args, **kwargs)
        logger.debug("Some MetaStuff: In the wrapper after: %s < < < < < < < < < < < < < <" % args[0])

    return a_wrapper


def forgiving_wrapper(orig_func):
    @wraps(orig_func)
    def b_wrapper(self, *args, **kwargs):
        logger.debug("Other MetaStuff: In the other wrapper, before > > > > > > > > > > > > >")
        try:
            orig_func(self, *args, **kwargs)
        except Exception as e:
            # If the exception is not re-raised, this could/should be a warning of some kind
            logger.warn("+ + OH NO + + %s (notice that the test _passes_ unless re-raised)" % e)
        logger.debug("Other MetaStuff: In the other wrapper, after < < < < < < < < < < < < < <")

    return b_wrapper


class retry(object):
    """
    Parameters to the decorator: retries (required), wait time after failure (in seconds),
    patience (exponent to increase wait time - can be float)
    """

    def __init__(self, retries, wait=5, patience=2):
        """
        The constructor takes the decorator's arguments. I don't see it doing much else except
        maybe munging those arguments somehow.
        """
        logger.debug("Inside retry.__init__()")
        self.retries = retries
        self.wait = wait
        self.forgiveness = patience

        logger.debug("Retry arguments: Retries={}, Wait={}, Forgiveness={}".format(self.retries, self.wait,
                                                                                   self.forgiveness))

    def __call__(self, orig_func):
        """
        The callable takes the decorated function as its only argument, and is only called during the wrapping
        """
        logger.debug("Inside retry.__call__()")

        @wraps(orig_func)
        def wrapped_f(*args):

            logger.debug("In the retry wrapper, before > > > > > > > > > > > > >")

            # This makes the test name (description) of the last executed test empty,
            # so the summary report falls back to the generator function name plus args
            self.__call__.__func__.description = ""

            # We want to wait _before_ trying the test
            wait_seconds = 0

            # This help make the log more readable. The last part drops the 'self' ref from the args
            # then joins the tuple elements into a nice string without the trailing comma you get from "str(tuple)"
            func_signature = "{}({})".format(orig_func.__name__, ', '.join(map(str, args[1:])))
            for attempt_count in range(1, self.retries + 1):
                try:
                    # No need to warn on the first attempt
                    if wait_seconds > 0:
                        logger.warning(
                            "Waiting {} seconds before next attempt...".format(wait_seconds))
                        sleep(wait_seconds)
                    logger.info(
                        "Starting attempt #{} of {}.".format(attempt_count, func_signature))
                    # NOTE: Execute the actual function with generated parameter(s)
                    orig_func(*args)
                    logger.info("{} succeeded.".format(func_signature))
                    # It worked, no need to retry :)
                    break
                except Exception as e:
                    # TODO: Generally, swallowing all exceptions is bad; the handled exceptions should be specific
                    # TODO: Differentiate between "retriable" exceptions and completely bollocks situations
                    # TODO: A tuple of retriable exception types would need to be passed in

                    # This kind of exception will skip the test instead of failure or error:
                    # raise SkipTest("No worries, I just don't like two.")

                    logger.warning(
                        "Attempt #{} of {} had an error: {}".format(attempt_count, func_signature, e))
                    wait_seconds = int(self.wait * math.pow(self.forgiveness, (attempt_count - 1)))
                    # Try again; this uses up one of our "retries"
                    continue
            else:
                # We have run out of retries without success, so raise an exception.
                message = "Maximum allowed retries ({}) exhausted for {}.".format(
                    self.retries, func_signature)
                logger.error(message)
                raise RetryMaximumAttemptsException(message)

            logger.debug("In the retry wrapper, after < < < < < < < < < < < < < <")

        return wrapped_f


class RetryMaximumAttemptsException(Exception):
    pass
