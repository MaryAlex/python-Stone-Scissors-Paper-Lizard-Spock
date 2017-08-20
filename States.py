from enum import Enum


# Length of it must always be odd
class States(Enum):
    Stone = 0
    Spock = 1
    Paper = 2
    Lizard = 3
    Scissors = 4


STATES_LEN = len(States)
