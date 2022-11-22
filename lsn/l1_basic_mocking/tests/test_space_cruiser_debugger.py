from unittest import TestCase
from unittest.mock import patch
from lsn.l1_basic_mocking.app.script import debug_space_cruiser, get_universe_hash, check_microverse_battery, check_quantum_carburetor


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

    # Exercise l1_B_1
    def test_space_cruiser_debugging_2(self):
        # hint: review debug_space_cruiser and mock.patch specific functions
        with (patch('lsn.l1_basic_mocking.app.script.get_universe_hash', return_value=67132),
              patch('lsn.l1_basic_mocking.app.script.check_quantum_carburetor', return_value=False)):
            self.assertFalse(debug_space_cruiser())
        # hint: review debug_space_cruiser and mock.patch specific functions
        with (patch('lsn.l1_basic_mocking.app.script.get_universe_hash', return_value=67132),
              patch('lsn.l1_basic_mocking.app.script.check_quantum_carburetor', return_value=True)):
            self.assertTrue(debug_space_cruiser())

    # Exercise l1_C
    @patch('lsn.l1_basic_mocking.app.script.get_universe_hash')
    def test_check_microverse_battery(self, mock_universe_hash_fun):
        mock_universe_hash_fun.return_value = 67132
        self.assertEqual(check_microverse_battery(), True)

        for i in range(-1, 4):
            self.assertEqual(check_microverse_battery(i), True)

        with self.assertRaises(Exception):
            check_microverse_battery(4)