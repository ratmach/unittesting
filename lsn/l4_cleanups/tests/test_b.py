from unittest import TestCase

from lsn.l4_cleanups.app.script import get_universe_compensation


class UniverseHolidayCount(TestCase):
    def test(self):
        self.assertEqual(get_universe_compensation(1000), 393800)
