import time
import re
import copy


def generate_timestamp():
    """
    Return a millisecond integer timestamp.
    """
    return int(time.time() * 10**3)
