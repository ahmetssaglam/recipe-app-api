# import os
# import sys
#
# print(os.path.dirname(os.path.realpath(__file__)))
# sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../"))
# print(sys.path)

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    def test_add(self):
        res = calc.add(5, 3)
        self.assertEqual(res, 8)

    def test_sub(self):
        res = calc.sub(5, 3)
        self.assertEqual(res, 2)
