import logging

from lsn.l1_basic_mocking.conf import Universes, UNIVERSE

logger = logging.getLogger(__name__)


def check_quantum_carburetor() -> bool:
    if UNIVERSE != Universes.C137:
        raise Exception("You cannot just add a sci-fi word to a car word and hope it means something")
    return True


def check_microverse_battery(level=0) -> bool:
    if level > 3:
        raise Exception(
            "Please put a spatially tessellated void inside a modified temporal field until a planet"
            " develops an intelligent life. Then introduce Gooblebox (or equivalent) which generates electricity"
            "that powers everything in their society and the levels above")
    if level == 1:
        logger.info(f"Checking MicroVerse for {get_universe_hash(UNIVERSE)}")
    if level == 2:
        logger.info(f"Checking MiniVerse for {get_universe_hash(UNIVERSE)}")
    if level == 3:
        logger.info(f"Checking TeenyVerse for {get_universe_hash(UNIVERSE)}")
        return True
    return check_microverse_battery(level=level + 1)


def get_universe_hash(universe) -> int:
    a, b = universe.split("-")
    return ord(a) * 1000 + int(b)


def debug_space_cruiser():
    return check_quantum_carburetor() and check_microverse_battery(level=1)
