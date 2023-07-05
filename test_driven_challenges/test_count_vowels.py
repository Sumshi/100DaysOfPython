#!/usr/bin/python3

import unittest

count_vowels = __import__('count_vowels').count_vowels

class TestCountVowel(unittest.TestCase):
    def test_vowels(self):
        assert count_vowels("hello") == 2

    def test_empty_string(self):
        assert count_vowels("") == 0

    def test_one_vowel(self):
        assert count_vowels("python"), 1

    def test_int(self):
        assert count_vowels(123), 1

    def test_error(self):
        with self.assertRaises(TypeError):
            count_vowels(1)


if __name__ == "main":
    unittest.main()
