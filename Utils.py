import hashlib
import hmac
from binascii import hexlify

import os

from States import STATES_LEN

SHA_LEN = 256


def HMAC_SHA(data):
    key = hexlify(os.urandom(SHA_LEN))
    hash_obj = hmac.new(key, bytes(data), hashlib.sha256)
    return hash_obj.hexdigest()


# State win half of all states after it
# And lose to half of all states before it
# Expected that STATES_LEN always odd
def is_win(player, computer):
    if player % STATES_LEN == computer % STATES_LEN:
        return "It's tie!"
    half_of_states = int((STATES_LEN + 1) / 2)
    for i in range(1, half_of_states):
        if (player + i) % STATES_LEN == computer % STATES_LEN:
            return "Computer wins!"
    return "Player wins!"
