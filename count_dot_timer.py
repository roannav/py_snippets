#!/usr/bin/env python3
import time


# prints 1 dot for every elapsed sec.
# It stops after 'sec' seconds have past.
def count_down_timer(sec):
    assert sec >= 0, \
        f"count_down_timer() expects non-negative int, but {sec} was given"

    while(sec):
        time.sleep(1)
        # end='', to continue printing on the same line.
        # However, using the end parameter, tells it to buffer.
        # flush=True, will stop buffering and instead immediately print.
        print('.', end='', flush=True)
        sec -= 1


# prints 1 dot for every elapsed sec.
# It continues forever.
def count_up_timer():
    while(True):
        time.sleep(1)
        print('.', end='', flush=True)


count_down_timer(3)
#count_down_timer(-1)   # will generate AssertionError
#count_up_timer()
