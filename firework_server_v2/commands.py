import unittest

from flask import Blueprint

tests = Blueprint("tests", __name__)


@tests.cli.command()
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover("test", pattern="test*.py")
    tests_methods = unittest.TestLoader().discover("test/test_methods", pattern="test*.py")
    suite = unittest.TestSuite()
    suite.addTest(tests) 
    suite.addTest(tests_methods) 

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        return 0
    return 1
