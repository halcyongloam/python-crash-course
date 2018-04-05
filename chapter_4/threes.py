# print the multiples of three from 3 to 30
threes = [num for num in range(3, 30, 3)]
for num in threes:
    print(num)

# print the first, middle, and last three numbers of the list
print('\nThe first three numbers are:')
for num in threes[:3]:
    print(num)

print('\nThe middle three numbers are:')
for num in threes[3:-3]:
    print(num)

print('\nThe last three numbers are:')
for num in threes[-3:]:
    print(num)
