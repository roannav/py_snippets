# Function to_standard_date(s):
# INPUT: s is a string in a date format
#
# Converts other date formats 
# to Month_name DD, YYYY   (aka Month_name Month_day_number, Year)
# eg July 2, 1999
# or to Month_name, YYYY if the day is not given  (eg July, 1999)

# Detects and then converts these formats:
# Month_name DD, YYYY
# Month_name DD YYYY
# DD Month_name YYYY
# YYYY MM DD
# YYYY/MM/DD or YYYY-MM-DD
# MM DD YYYY
# MM/DD/YYYY or MM-DD-YYYY
#
# Also incomplete dates:
# YYYY
# Month_name, YYYY
# Month_name YYYY
# YYYY, Month_name
# YYYY Month_name
# MM YYYY
# MM/YYYY or MM-YYYY
# YYYY MM
# YYYY/MM or YYYY-MM
#
# To avoid confusion, with the month or day, only 4 digit years are valid, 
# not 2 digit years.

import re

date_regex = re.compile(r'''
    (([ADFJMSON][a-z]+)\.?\s+(\d{1,2}),?\s+(\d{4})) |  # Month_name DD, YYYY or
                                                       # Month_name DD YYYY
    ((\d{1,2})\s+([ADFJMSON][a-z]+)\.?\s+(\d{4})) |    # DD Month_name YYYY
    ((\d{4})\s+(\d{1,2})\s+(\d{1,2})) |                # YYYY MM DD
    ((\d{4})\s*[/-]?\s*(\d{1,2})\s*[/-]?\s*(\d{1,2})) |  # YYYY/MM/DD or 
                                                         # YYYY-MM-DD
    ((\d{1,2})\s+(\d{1,2})\s+(\d{4})) |                  # MM DD YYYY
    ((\d{1,2})\s*[/-]?\s*(\d{1,2})\s*[/-]?\s*(\d{4}))    # MM/DD/YYYY or 
                                                         # MM-DD-YYYY
    ''', re.VERBOSE)


# month and year only; no day
month_year_regex = re.compile(r'''
    (([ADFJMSON][a-z]+)\.?,?\s+(\d{4})) |    # Month_name, YYYY or
                                             # Month_name YYYY
    ((\d{4}),?\s+([ADFJMSON][a-z]+)\.?) |    # YYYY, Month_name 
                                             # YYYY Month_name
                   
    ((\d{1,2})\s+(\d{4})) |                  # MM YYYY
    ((\d{1,2})\s*[/-]?\s*(\d{4})) |          # MM/YYYY or MM-YYYY
    ((\d{4})\s+(\d{1,2})) |                  # YYYY MM
    ((\d{4})\s*[/-]?\s*(\d{1,2}))            # YYYY/MM or YYYY-MM
    ''', re.VERBOSE)


# YYYY
year_only_regex = re.compile(r'\d{4}')


# MM
numeric_month_only_regex = re.compile(r'\d{1,2}')



VALID_DATE_STRS = [
    "January 1, 2022",
    "January 1 2022",
    "1 January 2022",
    "01 Jan 2022",
    "01 Jan. 2022",
    "2022 1 1",
    "2022 01 01",
    "1 1 2022",
    "01 01 2022",
    "2022 / 1 / 1",
    "2022/01/01",
    "1/1/2022",
    "01 / 01 / 2022",
    "2022-01-01",
    "1-1-2022"
]

VALID_MONTH_YEAR_STRS = [
    "January, 2022",
    "Jan, 2022",
    "Jan., 2022",
    "January 2022",
    "Jan 2022",
    "Jan. 2022",
    "2022, January",
    "2022, Jan",
    "2022, Jan.",
    "2022 January",
    "2022 Jan",
    "2022 Jan.",
    "1 2022",
    "1/2022",
    "1-2022",
    "2022 1",
    "2022/1",
    "2022-1"
]


# It's a year, if it's not part of date or month format and it looks 
# like a year.
def is_year_only(s):
    return date_regex.search(s) == None and \
           month_year_regex.search(s) == None and \
           year_only_regex.search(s) != None


# It's a month and year format, if it's not part of full date format 
# and it looks like a month and year.
def is_month_and_year_only(s):
    return date_regex.search(s) == None and \
           month_year_regex.search(s) != None


# It's a month, day, and year format
def is_full_date(s):
    return date_regex.search(s) != None



# Convert months that are written as words, abbreviations or numbers 
# into the full month name.
#
# INPUT: s: a string that represents a month
#           in the format of a 1 or 2 digit number
#           or a month name that may be abbreviated or not.
# Since "Ju" can be "June" or "July", this will require all abbreviations
# to be at least 3 letters.
def to_month_name(s):
    MONTH_NAMES = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"]

    txt = s
    if len(s) >= 1:
        if s[-1] == '.':   # remove the last char, if it's '.'
            txt = s[:-1]
        txt = txt.title()  # Capitalize the first letter. 
                           # Make the other letters lowercase.

    if s.isdigit() and len(s)<=2:    # 1 or 2 digit number
        n = int(s)
        if n <= 12:
            return MONTH_NAMES[n - 1] 

    elif txt.isalpha() and len(txt) >= 3:  # a word, at least 3 letters long
        for i,m in enumerate(MONTH_NAMES):
            if m.startswith(txt):
                return MONTH_NAMES[i]

    print(f"WARNING: to_month_name(): could not convert \'{s}\' into a month name.")
    return None



def to_standard_date(s):
    if is_year_only(s):
        return s

    elif is_month_and_year_only(s):
        match = month_year_regex.search(s)
        #print(match.groups())
        month = match.group(2) or match.group(6) or match.group(8) or \
            match.group(11) or match.group(15) or match.group(18)
        month = to_month_name(month)
        #print(f"Month is {month}\n\n")

        year = match.group(3) or match.group(5) or match.group(9) or \
            match.group(12) or match.group(14) or match.group(17)
        #print(f"Year is {year}\n\n")
        return month + ", " + year

    elif is_full_date(s):
        match = date_regex.search(s)
        #print(match.groups())

        month = match.group(2) or match.group(7) or match.group(11) or \
            match.group(15) or match.group(18) or match.group(22)
        month = to_month_name(month)
        #print(f"Month is {month}\n\n")

        day = match.group(3) or match.group(6) or match.group(12) or \
            match.group(16) or match.group(19) or match.group(23)
        if day[0] == '0':   # remove leading 0
            day = day[1]
        #print(f"Day is {day}\n\n")

        year = match.group(4) or match.group(8) or match.group(10) or \
            match.group(14) or match.group(20) or match.group(24)
        #print(f"Year is {year}\n\n")

        return month + " " + day + ", " + year



def test_date_regex():
    for s in VALID_DATE_STRS:
        match = date_regex.search(s)
        print(match.group())

    print("\n2022 is full date?", is_full_date("2022"))
    print("May, 2022 is full date?", is_full_date("May, 2022"))
    print("May 9, 2022 is full date?", is_full_date("May 9, 2022"))
    print("")



# Month_name, YYYY
# Month_name YYYY
# YYYY, Month_name
# YYYY Month_name
# MM YYYY
# MM/YYYY or MM-YYYY
# YYYY MM
# YYYY/MM or YYYY-MM
def test_month_year_regex():
    for s in VALID_MONTH_YEAR_STRS:
        match = month_year_regex.search(s)
        print(match.group())

    
    # it will still match the month and year regex,
    # even if it is part of a full month-day-year date
    test_strs = [
        "1-1-2022"
    ]
    for s in test_strs:
        match = month_year_regex.search(s)
        print(match.group())

    print("\n2022 is month and year only?", is_month_and_year_only("2022"))
    print("May, 2022 is month and year only?", 
      is_month_and_year_only("May, 2022"))
    print("May 9, 2022 is month and year only?", 
      is_month_and_year_only("May 9, 2022"))
    print("")



def test_year_only_regex():
    # it will still match the year regex,
    # even if it is part of a full month-day-year date
    match = year_only_regex.search("1-1-2022")
    print(match.group())   # 2022

    print("\n2022 is year only?", is_year_only("2022"))
    print("May, 2022 is year only?", is_year_only("May, 2022"))
    print("May 9, 2022 is year only?", is_year_only("May 9, 2022"))
    print("")



def test_to_month_name():
    print("....", to_month_name("02"))
    print("....", to_month_name("7"))
    print("....", to_month_name("90"))
    print("....", to_month_name(""))
    print("....", to_month_name("A"))
    print("....", to_month_name("Sept."))
    print("....", to_month_name("September"))
    print("....", to_month_name("Octo"))
    print("....", to_month_name("jul"))



def test():
    match = month_year_regex.search("May, 2022")
    print(match.groups())

    match = month_year_regex.search("2022, May")
    print(match.groups())

    match = month_year_regex.search("05 2022")
    print(match.groups())


    print("\n\nto_standard_date(s)")
    
    print(to_standard_date("2022"))

    for s in VALID_MONTH_YEAR_STRS:
        print(to_standard_date(s))

    for s in VALID_DATE_STRS:
        print(to_standard_date(s))



def run_tests():
    test_date_regex()
    test_month_year_regex()
    test_year_only_regex()
    test_to_month_name()
    test()



run_tests()
