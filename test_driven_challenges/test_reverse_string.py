#!/usr/bin/python3

"""test file for reversing a string function"""

import unittest
reverse_string = __import__('reverse_string').reverse_string

class TestReverseString(unittest.TestCase):

    def testReverse(self):
        self.assertEqual(reverse_string("Hello"), "olleH")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("1234"), "4321")
        self.assertEqual(reverse_string("mmm"), "mmm")

    def test_error(self):
        with self.assertRaises(TypeError):
            reverse_string(1, "1")

if __name__ == "main":
    unittest.main()
