import logging

from lsn.l1_basic_mocking.conf import Universes, UNIVERSE


class SpaceCruiser:
    def __init__(self, universe, logger):
        self.universe = universe
        self.logger = logger

    @staticmethod
    def get_universe_hash(universe) -> int:
        a, b = universe.split("-")
        return ord(a) * 1000 + int(b)

    def check_quantum_carburetor(self) -> bool:
        if self.universe != Universes.C137:
            raise Exception("You cannot just add a sci-fi word to a car word and hope it means something")
        return True

    def check_microverse_battery(self, level=0) -> bool:
        if level > 3:
            raise Exception(
                "Please put a spatially tessellated void inside a modified temporal field until a planet"
                " develops an intelligent life. Then introduce Gooblebox (or equivalent) which generates electricity"
                "that powers everything in their society and the levels above")
        if level == 1:
            self.logger.info(f"Checking MicroVerse for {SpaceCruiser.get_universe_hash(UNIVERSE)}")
        if level == 2:
            self.logger.info(f"Checking MiniVerse for {SpaceCruiser.get_universe_hash(UNIVERSE)}")
        if level == 3:
            self.logger.info(f"Checking TeenyVerse for {SpaceCruiser.get_universe_hash(UNIVERSE)}")
            return True
        return self.check_microverse_battery(level=level + 1)

    def debug_space_cruiser(self):
        return self.check_quantum_carburetor() and self.check_microverse_battery(level=1)


if __name__ == "__main__":
    cruiser = SpaceCruiser(universe=UNIVERSE, logger=logging.getLogger(__name__))
    cruiser.debug_space_cruiser()
