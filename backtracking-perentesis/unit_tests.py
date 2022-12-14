import unittest
import pytest

import generate
import validate
# Tests adapted from `problem-specifications//canonical-data.json`


class parentheses(unittest.TestCase):
    @pytest.mark.task(taskno=1)
    def test_validate1(self):
        self.assertEqual(validate.is_valid_regular1('(())'), True)
        self.assertEqual(validate.is_valid_regular2('(())'), True)

    @pytest.mark.task(taskno=2)
    def test_validate2(self):
        self.assertEqual(validate.is_valid_regular1('(()))'), False)
        self.assertEqual(validate.is_valid_regular2('(()))'), False)
    
    @pytest.mark.task(taskno=3)
    def test_validate3(self):
        self.assertEqual(validate.is_valid_regular1('(())('), False)
        self.assertEqual(validate.is_valid_regular2('(())('), False)

    @pytest.mark.task(taskno=4)
    def test_validate4(self):
        self.assertEqual(validate.is_valid_regular1('()(())'), True)
        self.assertEqual(validate.is_valid_regular2('()(())'), True)

    @pytest.mark.task(taskno=5)
    def test_validate5(self):
        self.assertEqual(validate.is_valid_regular1('()(()()'), False)
        self.assertEqual(validate.is_valid_regular2('()(()()'), False)

    @pytest.mark.task(taskno=6)
    def test_generate(self):
        self.assertEqual(generate.gen(2), ['(())', '()()'])
        self.assertEqual(generate.gen(3), ['((()))', '(()())', '(())()', '()(())', '()()()'])

    @pytest.mark.task(taskno=7)
    def test_validate7(self):
        self.assertEqual(validate.is_valid_any('({[]})'), True)
        self.assertEqual(validate.is_valid_any('({[])})'), False)

    @pytest.mark.task(taskno=8)
    def test_validate8(self):
        self.assertEqual(validate.is_valid_any(')({[]})'), False)
        self.assertEqual(validate.is_valid_any('({[])}){'), False)
