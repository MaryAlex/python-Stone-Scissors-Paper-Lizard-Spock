import hashlib

from States import STATES_LEN


def hash_md5(data):
    hash_id = hashlib.md5()
    hash_id.update(repr(data).encode('utf-8'))
    return hash_id.hexdigest()


# State win half of all states after it
# And lose to half of all states before it
# Expected that STATES_LEN always odd
def is_win(player, computer):
    if player % STATES_LEN == computer % STATES_LEN:
        return "It's tie!"
    half_of_states = int((STATES_LEN + 1) / 2)
    for i in range(1, half_of_states):
        if (player + i) % STATES_LEN == computer % STATES_LEN:
            return "Player wins!"
    return "Computer wins!"
