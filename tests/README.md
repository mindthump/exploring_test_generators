For decorators to wrap around each test in a set of generated tests (using `yield`), the decorator must be wrapped
around the function that is yielded to. If it is wrapped around the original test generator, it will only execute
once for the generator itself.

Actions in those decorators that follow an assertion failure or other exception will never run, unless the exception is handled right
there in the decorator. If it is handled there and not re-raised the test will pass. That is the nature of python
exceptions; they continue execution immediately following the `try` where the exception is handled, so if it
gets handled higher up by the test framework the decorator will never get control back.