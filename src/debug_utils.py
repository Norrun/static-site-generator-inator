import unittest

def disable_maxDiff(func):
    def wrapper(self: unittest.TestCase):
        self.maxDiff = None
        return func(self)
    return wrapper

def disable_test(reason):
    def decorator(func):
        def wrapper(self: unittest.TestCase):
            self.skipTest(reason)
            return func(self)
        return wrapper
    return decorator