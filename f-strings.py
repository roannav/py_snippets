# NOTE: Python 3.8 has the = shortcut in f-strings
# eg  x=2;  print(f'{x=}')  
# ===> x=2


song = {
    "title": "Fly Me to the Moon",
    "genre": "Jazz",
    "recorded_year": 1954 
}

# For the multiline f-string,
# note the () contains all the strings
# and there are no ','s at the end of each line
output = (
    f'Title is {song["title"]}\n'
    f'Genre is {song["genre"]}\n'
    f'Recorded Year is {song["recorded_year"]}\n'
)

print(output)


# $10 -> $10.00
dollars = 10
print(f"You have ${dollars:.2f}")

# Add , for every thousand in the number
# 123456789 -> 123,456,789 
revenue = 123456789
print(f"Revenue is ${revenue:,}")

# Add leading 0s
# 9:00 -> 09:00
meeting_time = 9
print(f"Meeting time is {meeting_time:02}:00")

# No leading 0, since the time is already 2 digits long
meeting_time = 13
print(f"Meeting time is {meeting_time:02}:00\n")

# within a 40 column space, center the text
txt = "Centered Text"
print(f"{txt:^40}")

# within a 40 column space, center the text
# and use # as a filler
txt = "  Centered Text  "
print(f"{txt:#^40}")

# within a 40 column space, left-align the text
txt = "Left-aligned Text"
print(f"{txt:<40}")

# within a 40 column space, right-align the text
txt = "Right-aligned Text"
print(f"{txt:>40}")

