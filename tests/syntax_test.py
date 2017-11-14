"""This file contains code for testing email validators

Running:
- `python3 -m maillist.tests.syntax_test`
"""


import unittest
import os

from ..validators import SyntaxValidator


class ValidatorsTest(unittest.TestCase):

    def setUp(self):
        fixtures_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures')
        self.valid_emails_filename = os.path.join(fixtures_dir, 'emails_syntax_valid.txt')
        self.invalid_emails_filename = os.path.join(fixtures_dir, 'emails_syntax_invalid.txt')
        self.validator = SyntaxValidator()

    def testValidatorBase(self):
        self.assertEqual(SyntaxValidator.colname(), 'Syntax')

    def testValid(self):
        with open(self.valid_emails_filename, 'r', encoding='utf-8') as fp:
            for line in fp:
                self.assertTrue(self.validator.is_valid(line.strip()))

    def testInValid(self):
        with open(self.invalid_emails_filename, 'r', encoding='utf-8') as fp:
            for line in fp:
                self.assertFalse(self.validator.is_valid(line.strip()))

    def testNull(self):
        self.assertFalse(self.validator.is_valid(None))


unittest.main()
