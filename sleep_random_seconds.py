# NOTE: src https://stackoverflow.com/questions/377454/how-do-i-get-my-python-program-to-sleep-for-50-milliseconds
# sleep() is not exactly accurate; could be 10 or 15 ms longer on some 
# platforms.  Things that affect precision: thread/process priority,
# CPU load avg, available memory, how busy the system is, etc.

# As of Python 3.5, sleep() will sleep AT LEAST the specified # of seconds.

import time
import random

# fixed amount of time sleep, specified by 'delay' seconds
def fixed_time_delay( delay):
    print("\nStart")
    time.sleep(delay)
    print(f"End.  It\'s {delay} seconds later")


# Sleep a random amount of seconds (given a range).
# It will wait between min_delay and max_delay seconds.
# IN: min_delay: minimum amount of time to wait
# IN: max_delay: maximum time to wait
# IN: decimal_point_precision:  
#       how many decimal points of precision the time delay will be
def random_time_delay( min_delay, max_delay, decimal_point_precision):
    print("\nStart")
    random_time_delay = round(random.uniform( min_delay, max_delay), 
                              decimal_point_precision)
    time.sleep( random_time_delay)
    print(f"End.  It\'s {random_time_delay} seconds later.")


# random time delay, between 2 to 5 seconds,
# rounded to 3 decimal places
def test_random_time_delay():
    print("\nStart")
    random_time_delay = round(random.uniform(2, 5), 3)
    time.sleep( random_time_delay)
    print(f"End.  It\'s {random_time_delay} seconds later.")


def run_tests():
    fixed_time_delay( 1.7)
    random_time_delay( 1, 3, 3)
    #random_time_delay( 8, 15, 3)
    test_random_time_delay()


run_tests()
