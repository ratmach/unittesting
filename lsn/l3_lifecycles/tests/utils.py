from random import random
from unittest import TestCase


class SetUpTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.value = random()
        cls.expected_value = cls.value

    def tearDown(self):
        self.assertEqual(self.value, self.expected_value)


class SetUpClassTest(TestCase):
    def setUp(self):
        self.value = random()
        self.expected_value = self.value

    def tearDown(self):
        self.assertEqual(self.value, self.expected_value)


class TearDownTest(TestCase):
    def setUp(self) -> None:
        self.some_stuff = 1234

    def tearDown(self):
        self.assertEqual(getattr(self, "some_stuff", None), None)
