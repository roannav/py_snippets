# Convert other date formats 
# to Month_name DD, YYYY   (aka Month_name Month_day_number, Year)
# eg July 2, 1999
# or to Month_name YYYY, if the day is not given  (eg July, 1999)

# Detect and then convert these formats:
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
    ([ADFJMSON][a-z]+\.?\s+\d{1,2},?\s+\d{4}) |    # Month_name DD, YYYY or
                                                   # Month_name DD YYYY
    (\d{1,2}\s+[ADFJMSON][a-z]+\.?\s+\d{4}) |      # DD Month_name YYYY
    (\d{4}\s+\d{1,2}\s+\d{1,2}) |                  # YYYY MM DD
    (\d{4}\s*[/-]?\s*\d{1,2}\s*[/-]?\s*\d{1,2}) |  # YYYY/MM/DD or YYYY-MM-DD
    (\d{1,2}\s+\d{1,2}\s+\d{4}) |                  # MM DD YYYY
    (\d{1,2}\s*[/-]?\s*\d{1,2}\s*[/-]?\s*\d{4})    # MM/DD/YYYY or MM-DD-YYYY
    ''', re.VERBOSE)


# month and year only; no day
month_year_regex = re.compile(r'''
    ([ADFJMSON][a-z]+\.?,?\s+\d{4}) |    # Month_name, YYYY or
                                         # Month_name YYYY
    (\d{4},?\s+[ADFJMSON][a-z]+\.?) |    # YYYY, Month_name 
                                         # YYYY Month_name
                   
    (\d{1,2}\s+\d{4}) |                  # MM YYYY
    (\d{1,2}\s*[/-]?\s*\d{4}) |          # MM/YYYY or MM-YYYY
    (\d{4}\s+\d{1,2}) |                  # YYYY MM
    (\d{4}\s*[/-]?\s*\d{1,2})            # YYYY/MM/DD or YYYY-MM-DD
    ''', re.VERBOSE)


# YYYY
year_only_regex = re.compile(r'\d{4}')



def test_date_regex():
    test_strs = [
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

    for s in test_strs:
        match = date_regex.search(s)
        print(match.group())


# Month_name, YYYY
# Month_name YYYY
# YYYY, Month_name
# YYYY Month_name
# MM YYYY
# MM/YYYY or MM-YYYY
# YYYY MM
# YYYY/MM or YYYY-MM
def test_month_year_regex():
    test_strs = [
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
        "2022-1",
        "1-1-2022"
    ]
    # it will still match the month and year regex,
    # even if it is part of a full month-day-year date

    for s in test_strs:
        match = month_year_regex.search(s)
        print(match.group())



def test_year_only_regex():
    # it will still match the year regex,
    # even if it is part of a full month-day-year date
    match = year_only_regex.search("1-1-2022")
    print(match.group())   # 2022


test_date_regex()
test_month_year_regex()
test_year_only_regex()


