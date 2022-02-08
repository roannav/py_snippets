#! python3

import re

# IN: n: string, which might look like a number
# OUT: whether it is a number
# commas are optional, but if they are used, it should be every 3 digits
def is_number(n):
    # 0 is separate, to avoid matching -0
    num_regex = re.compile(r'^(0|-?\d+|(-?\d{1,3}(,\d{3})*))$')
    return num_regex.search(n) != None

# IN: n: string, which might look like a number
# not just any number...
# only returns True if there is at least 1 comma
# OUT: whether it is a number
def is_number_with_commas(n):
    num_regex = re.compile(r'^-?\d{1,3}(,\d{3})+$')
    return num_regex.search(n) != None

def run_test_is_number(n, answer):
    # print message, if it fails the test
    if is_number(n) != answer:
        print(f'FAIL: is_number({n})')
    else: # print dot (on the same line), if it passes the test
        print('.', end='')
    
def run_test_is_number_with_commas(n, answer):
    # print message, if it fails the test
    if is_number_with_commas(n) != answer:
        print(f'FAIL: is_number_with_commas({n})')
    else: # print dot (on the same line), if it passes the test
        print('.', end='')
    
def run_tests():
    for n in ['1,000', '34,235', '-178,897,451',
              0, 1, -1, 889]:
        run_test_is_number(str(n), True)

    for n in ['1,2', '34,23,123', '3456,234,678', '3,2345']:
        run_test_is_number(str(n), False)

    for n in ['1,000', '34,235', '-178,897,451']:
        run_test_is_number_with_commas(str(n), True)

    for n in [0, 1, -1, 889, '1,2', '34,23,123', '3456,234,678', '3,2345']:
        run_test_is_number_with_commas(str(n), False)



run_tests()
