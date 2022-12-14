from lsn.l1_basic_mocking.conf import Universes


def get_universe():
    return Universes.C137


def get_universe_holidays():
    universe = get_universe()
    if universe == Universes.C137:
        return 24
    raise Exception("no idea honestly")


def get_universe_calendar_days():
    universe = get_universe()
    if universe == Universes.C137:
        return 365
    raise Exception("no idea honestly")


def get_universe_compensation(salary):
    return (get_universe_holidays() * salary * 1.2) + (get_universe_calendar_days() * salary)
