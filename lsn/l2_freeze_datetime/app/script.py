import datetime
import logging
import time
from random import random

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def try_stabilize_time():
    raise Exception("Failed to stabilize time")


def unfreeze_time():
    time_start = datetime.datetime.now()
    time.sleep(1)
    time_end = datetime.datetime.now()
    time_passed = (time_end - time_start).microseconds
    if time_passed > 0:
        raise Exception("Failed to unfreeze time, as it was never frozen")
    return True


def clean_the_house():
    logger.info("Cleaning the house")
    time.sleep(0.005)


def repair_the_party_damage():
    logger.info("Repairing party damage")
    time.sleep(0.005)


def carve_pumpkins():
    logger.info("Carving pumpkins")
    time.sleep(0.005)


def steal_things_from_best_buy():
    logger.info("Stealing things from best buy")
    time.sleep(0.005)


def watch_titanic():
    logger.info("Watching titanic")
    time.sleep(0.005)


def dance():
    logger.info("Dancing")
    time.sleep(0.005)


def vacuum_mom_and_dad():
    logger.info("Vacuuming Beth and Jerry")
    time.sleep(0.005)


def forget_to_put_mattress_under_mr_benson():
    logger.info("Forgetting to put the mattress under mr Benson")
    time.sleep(0.005)


def freeze_time():
    time_start = datetime.datetime.now()

    for day_count in range(6 * 30):
        logger.info(f"[freeze_time] day {day_count} of {6 * 30} ")
        if random() > 0.5:
            clean_the_house()
        if random() > 0.5 and day_count < 30:
            repair_the_party_damage()
        if random() > 0.5 and 40 < day_count < 45:
            carve_pumpkins()
        if random() > 0.8:
            steal_things_from_best_buy()
        if random() > 0.9:
            watch_titanic()
            dance()
        if random() > 0.5:
            vacuum_mom_and_dad()
        if random() > 0.5:
            forget_to_put_mattress_under_mr_benson()

    time_end = datetime.datetime.now()
    time_passed = (time_end - time_start).microseconds
    if time_passed > 0:
        raise Exception("Jerry and Beth caught you")
    unfreeze_time()
    logger.info(
        "Here is 500$ cash in unmarked moneys, i'm gonna just put it on the floor and kick it over to ya, you guys go nuts")
    return try_stabilize_time()
