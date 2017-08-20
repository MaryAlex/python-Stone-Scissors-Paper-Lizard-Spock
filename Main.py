import random

from Utils import is_win, hash_md5

RANDOM_TO_NUMBER = 10000

computers_number = random.randrange(RANDOM_TO_NUMBER)
print(hash_md5(computers_number))
player_choose = int(input("You choose?(Stone = 0, Spock = 1, Paper = 2, Lizard = 3, Scissors = 4)\n"))
print(is_win(player_choose, computers_number))
