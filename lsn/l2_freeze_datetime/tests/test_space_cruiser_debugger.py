from unittest import TestCase

from lsn.l2_freeze_datetime.app.script import freeze_time


class TestSpaceCruiserDebugger(TestCase):
    # Exercise l2_A
    def test_time_freezing(self):
        self.assertTrue(freeze_time())
