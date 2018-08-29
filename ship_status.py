from enum import Enum


class ShipStatus(Enum):
    NO_SHIP = 0
    SHIP = 1
    MISS = 2
    HIT = 3
    SUNK = 4
