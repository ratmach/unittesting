import logging

from lsn.l1_basic_mocking.app.script_oop import SpaceCruiser
from lsn.l1_basic_mocking.conf import UNIVERSE
from lsn.l1_basic_mocking.tests.utils import OOPOnlyTestCase
from unittest.mock import patch

class TestOOPSpaceCruiserDebugger(OOPOnlyTestCase):
    # Exercise l1_A1
    def test_universe_hashing_algorithm(self):
        # hint: check outputs for get_universe_hash algorithm
        self.assertEqual(SpaceCruiser.get_universe_hash('C-137'), 67137)
        self.assertEqual(SpaceCruiser.get_universe_hash('D-137'), 68137)

    # Exercise l1_B1
    @patch('lsn.l1_basic_mocking.app.script_oop.SpaceCruiser.check_quantum_carburetor')
    @patch('lsn.l1_basic_mocking.app.script_oop.SpaceCruiser.get_universe_hash')
    def test_space_cruiser_debugging(self, mock_universe_hash, mock_check_quantum_carburetor):
        cruiser = SpaceCruiser(universe=UNIVERSE, logger=logging.getLogger(__name__))
        # hint: review debug_space_cruiser and mock.patch specific functions
        mock_universe_hash.return_value = 67137
        mock_check_quantum_carburetor.return_value = False
        self.assertFalse(cruiser.debug_space_cruiser())
        # hint: review debug_space_cruiser and mock.patch specific functions
        mock_check_quantum_carburetor.return_value = True
        self.assertTrue(cruiser.debug_space_cruiser())

    # Exercise l1_C1
    def test_check_microverse_battery(self):
        cruiser = SpaceCruiser(universe=UNIVERSE, logger=logging.getLogger(__name__))

        with patch.object(SpaceCruiser, 'get_universe_hash', return_value=67123):
            self.assertEqual(cruiser.check_microverse_battery(), True)

            with self.assertRaises(Exception):
                cruiser.check_microverse_battery(4)
