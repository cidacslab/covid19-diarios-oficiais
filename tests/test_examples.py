# see https://github.com/CleanCut/green#unit-test-structure-tutorial
import unittest

## TODO: move unit tests from the main code to here

class TestExamples(unittest.TestCase):
    def test_equals(self):
        "Example test using equality"
        self.assertEqual(2, 2)

    def test_fail(self):
        "this test should always fail."
        "comment out"
        self.assertEqual(1,0)
