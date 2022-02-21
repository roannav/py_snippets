# Convert other date formats 
# to Month_name DD, YYYY   (aka Month_name Month_day_number, Year)
# eg July 2, 1999

# Detect and then convert these formats:
# YYYY MM DD

import re

dateRegex = re.compile(r'\d{4}\s+\d{2}\s+\d{2}')

match = dateRegex.search("2022 01 01")
print(match.group())

