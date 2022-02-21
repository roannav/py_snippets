# Convert other date formats 
# to Month_name DD, YYYY   (aka Month_name Month_day_number, Year)
# eg July 2, 1999

# Detect and then convert these formats:
# Month_name DD, YYYY
# Month_name DD YYYY
# DD Month_name YYYY
# YYYY MM DD
# YYYY/MM/DD
# MM DD YYYY
# MM/DD/YYYY

import re

dateRegex = re.compile(r'''
    ([ADFJMSON][a-z]+\.?\s+\d{1,2},?\s+\d{4}) |  # Month_name DD, YYYY
                                                 # Month_name DD YYYY
    (\d{1,2}\s+[ADFJMSON][a-z]+\.?\s+\d{4}) |    # DD Month_name YYYY
    (\d{4}\s+\d{1,2}\s+\d{1,2}) |                # YYYY MM DD
    (\d{4}\s*/?\s*\d{1,2}\s*/?\s*\d{1,2}) |      # YYYY/MM/DD
    (\d{1,2}\s+\d{1,2}\s+\d{4}) |                # MM DD YYYY
    (\d{1,2}\s*/?\s*\d{1,2}\s*/?\s*\d{4})        # MM/DD/YYYY
    ''', re.VERBOSE)

match = dateRegex.search("January 1, 2022")
print(match.group())

match = dateRegex.search("January 1 2022")
print(match.group())

match = dateRegex.search("1 January 2022")
print(match.group())

match = dateRegex.search("01 Jan 2022")
print(match.group())

match = dateRegex.search("01 Jan. 2022")
print(match.group())

match = dateRegex.search("2022 1 1")
print(match.group())

match = dateRegex.search("2022 01 01")
print(match.group())

match = dateRegex.search("1 1 2022")
print(match.group())

match = dateRegex.search("01 01 2022")
print(match.group())

match = dateRegex.search("2022 / 1 / 1")
print(match.group())

match = dateRegex.search("2022/01/01")
print(match.group())

match = dateRegex.search("1/1/2022")
print(match.group())

match = dateRegex.search("01 / 01 / 2022")
print(match.group())

