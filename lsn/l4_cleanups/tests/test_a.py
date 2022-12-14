from unittest import TestCase
from unittest.mock import patch

from lsn.l4_cleanups.app.script import get_universe_holidays, get_universe_calendar_days, get_universe_compensation


class UniverseDaysCountHasFallback(TestCase):
    def setUp(self):
        self.mocked_calendar_days = patch("lsn.l4_cleanups.app.script.get_universe").start()

    def test_raises_exception(self):
        with self.assertRaises(Exception):
            get_universe_holidays()
        with self.assertRaises(Exception):
            get_universe_calendar_days()


class UniverseHolidayCount(TestCase):
    def test(self):
        self.assertEqual(get_universe_compensation(1000), 393800)
