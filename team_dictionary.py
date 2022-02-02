teams = {"Rams": 3, "BlueJays": 8, "Ducks": 7}

for team, rank in teams.items():
    print(f'{team} has a rank of {rank}')

# f-strings
# :10 creates a column with width of 10 (space padded)
# strings are aligned left
# integers are aligned right
for team, rank in teams.items():
    print(f'{team:10}: {rank:10}')

# :d shows it's a decimal
for team, rank in teams.items():
    print(f'{team:10}: {rank:10d}')

for team, rank in teams.items():
    print(f'{rank:10}: {team:10}')

for team, rank in teams.items():
    print(f'{rank:10d}: {team:10}')
