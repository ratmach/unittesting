from dataclasses import dataclass
from random import random
from unittest import TestCase

from lsn.l1_basic_mocking.conf import Universes


@dataclass
class Jerry:
    origin: Universes
    name: str = "jerry"


class SetUpTest(TestCase):
    def test_default(self):
        pass

    def tearDown(self):
        self.assertNotEqual(self.jerry, None)
        self.assertEqual(self.jerry.name, "jerry")
        self.assertEqual(self.jerry.origin, Universes.C137)


class SetUpClassTest(TestCase):
    def test_default(self):
        pass

    @classmethod
    def tearDownClass(cls):
        assert (getattr(cls, "jerry", None) is not None)
        assert (getattr(cls, "jerry", None).name == "jerry")
        assert (getattr(cls, "jerry", None).origin == Universes.C137)


class TearDownTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.jerry = Jerry(origin=Universes.C137)

    def test_default(self):
        pass

    def doCleanups(self) -> None:
        self.assertEqual(getattr(self, "jerry", None), None)
        super().doCleanups()


class TearDownClassTest(TestCase):
    def setUp(self) -> None:
        self.jerry = Jerry(origin=Universes.C137)

    def test_default(self):
        pass

    @classmethod
    def doClassCleanups(cls) -> None:
        assert (getattr(cls, "jerry", None) is None)
        super().doClassCleanups()
