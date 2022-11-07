from unittest import TestCase

from lsn.l1_basic_mocking.app.script import debug_space_cruiser


class TestSpaceCruiserDebugger(TestCase):
    # Exercise l1_A
    def test_universe_hashing_algorithm(self):
        # hint: check outputs for get_universe_hash algorithm
        pass

    # Exercise l1_B
    def test_space_cruiser_debugging(self):
        print("nope")
        # hint: review debug_space_cruiser and mock.patch specific functions
        self.assertFalse(debug_space_cruiser())
        # hint: review debug_space_cruiser and mock.patch specific functions
        self.assertTrue(debug_space_cruiser())
