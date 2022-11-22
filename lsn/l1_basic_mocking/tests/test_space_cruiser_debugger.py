from unittest import TestCase
from unittest.mock import patch
from lsn.l1_basic_mocking.app.script import debug_space_cruiser, get_universe_hash


class TestSpaceCruiserDebugger(TestCase):
    # Exercise l1_A
    def test_universe_hashing_algorithm(self):
        # hint: check outputs for get_universe_hash algorithm
        self.assertEqual(get_universe_hash('C-132'), 67132)
        self.assertEqual(get_universe_hash('D-132'), 68132)


    # Exercise l1_B
    @patch('lsn.l1_basic_mocking.app.script.check_quantum_carburetor')
    @patch('lsn.l1_basic_mocking.app.script.get_universe_hash')
    def test_space_cruiser_debugging(self, mock_universe_hash_fun, mock_check_quantum_fun):
        # hint: review debug_space_cruiser and mock.patch specific functions
        mock_universe_hash_fun.return_value = 67132
        mock_check_quantum_fun.return_value = False
        self.assertFalse(debug_space_cruiser())
        # hint: review debug_space_cruiser and mock.patch specific functions
        mock_check_quantum_fun.return_value = True
        self.assertTrue(debug_space_cruiser())
