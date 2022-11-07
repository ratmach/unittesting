import logging

from lsn.l1_basic_mocking.app.script_oop import SpaceCruiser
from lsn.l1_basic_mocking.conf import UNIVERSE
from lsn.l1_basic_mocking.tests.utils import OOPOnlyTestCase


class TestOOPSpaceCruiserDebugger(OOPOnlyTestCase):
    # Exercise l1_A1
    def test_universe_hashing_algorithm(self):
        # hint: check outputs for get_universe_hash algorithm
        pass

    # Exercise l1_B1
    def test_space_cruiser_debugging(self):
        cruiser = SpaceCruiser(universe=UNIVERSE, logger=logging.getLogger(__name__))
        # hint: review debug_space_cruiser and mock.patch specific functions
        self.assertFalse(cruiser.debug_space_cruiser())
        # hint: review debug_space_cruiser and mock.patch specific functions
        self.assertTrue(cruiser.debug_space_cruiser())
