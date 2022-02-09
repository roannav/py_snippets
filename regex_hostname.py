#! python3

import re

# IN: s: string
# approximately checks that it looks like a valid website url hostname:
# with http://subdomain_(optional).domain_name.top_level_domain
# subdomain (if it exists) must have at least 1 character.
# the domain must have between 1 and 63 characters.
# top_level_domain can have numbers or letters and have length bet 2-6 chars.
# This version doesn't allow for hyphens.
# OUT: whether it is a hostname 
def is_hostname(s):
    reg = re.compile(r'''(
        ^https?://          # begins with a protocol
        ([a-z0-9]+\.)?      # subdomain
        ([a-z0-9]{1,63}\.)  # domain
        ([\w\d]{2,6})       # top level domain
        /?$                 # optional / at the end
    )''', re.VERBOSE | re.IGNORECASE)
    return reg.search(s) != None


def run_test_is_hostname(s, answer):
    # print message, if it fails the test
    if is_hostname(s) != answer:
        print(f'FAIL: is_hostname({s}) should be {answer}')
    else: # print dot (on the same line), if it passes the test
        print('.', end='')

    
def run_tests():

    true_tests = [
        'http://google.com', 
        'http://google.com', 
        'https://www.google.com',
        'https://wWw.gOlllE.coM/',
        'https://subdomain.google.com',
        'http://blog.google.biz',
        'http://ww2.sell2u.us',
        'http://w.s.us34/',
        'http://w.s.us345/',
        'http://w.s.us3456/',
    ]
    for s in true_tests:
        run_test_is_hostname(s, True)

    false_tests = [
        '//google.com',                # bad protocols
        '.://www.google.com',
        'https:://www.google.com',
        'http:/www.google.com',
        'httpss://www.google.com',
        'htp://ww2.sell2u.us',

        'https://www.google.com.a',    # too many .
        'http://.sell2u.us',           # . at beginning
        'http://sell2u.us.',           # . at end
        'https://www..google.com',
        'https://www.google..com',

        'https://www.go@ogle.com',     # domain name has characters that are 
        'https://www.goo(le.com',      # not letters or numbers
        'https://www.goog$e.com',
        'https://www.g\ngle.com',
        'https://www.g\tgle.com',
        'https://www.g.c^m',          # top level domain name has invalid chars

        'https://www.google.c',        # wrong length top level domain
        'https://www.google.c234567',

    ]
    for s in false_tests:
        run_test_is_hostname(s, False)


run_tests()
