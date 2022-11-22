from unittest import TestCase

from lsn.l1_basic_mocking.app.script import debug_space_cruiser, get_universe_hash


class TestSpaceCruiserDebugger(TestCase):
    # Exercise l1_A
    def test_universe_hashing_algorithm(self):
        # hint: check outputs for get_universe_hash algorithm
        self.assertEqual(get_universe_hash('C-132'), 67132)
        self.assertEqual(get_universe_hash('D-132'), 68132)


    # Exercise l1_B
    def test_space_cruiser_debugging(self):
        # hint: review debug_space_cruiser and mock.patch specific functions
        self.assertFalse(debug_space_cruiser())
        # hint: review debug_space_cruiser and mock.patch specific functions
        self.assertTrue(debug_space_cruiser())
