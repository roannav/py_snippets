data = [
    ['first_name', 'last_name', 'job', 'age'],
    ['Mary', 'Stevens', 'Mechanical Engineer', 30],
    ['Joe', 'Biden', 'President', 79],
    ['Kylie', 'Monroe', 'Singer', 18]
]

print("\nprint(*row, sep='...')")
for row in data:
    print(*row, sep='...')

print("\nprint(f'{row}')")
for row in data:
    print(f'{row}')

print("\nprint(*row)")
for row in data:
    print(*row)
