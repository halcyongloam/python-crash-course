# store a list of people I would like to invite to a dinner party, then print a
# message inviting each of them to dinner
guests = ['chris miller', 'nate belcher', 'cayden leicht']
message = ', you are invited to dinner at my place.'
count = 'I am inviting '
print(guests[0].title() + message)
print(guests[1].title() + message)
print(guests[2].title() + message)
print(count + str(len(guests)) + ' people')
# someone can no longer make it, remove them from the list and print their
# name, then add someone new and reinvite people
del guests[2]
print('\n' + 'Cayden Leicht can no longer make it '
      + 'on account of being in Shithole, Nebraska\n')

guests.append('michael patton')
print(guests[0].title() + message)
print(guests[1].title() + message)
print(guests[2].title() + message)
print(count + str(len(guests)) + ' people')

# I have found a bigger dinner table, announce so, and invite three more people
print('\nI have found a larger dinner table!\n')
guests.insert(0, 'michael banks')
guests.insert(2, 'abby meyer')
guests.append('emma loden')
print(guests[0].title() + message)
print(guests[1].title() + message)
print(guests[2].title() + message)
print(guests[3].title() + message)
print(guests[4].title() + message)
print(guests[5].title() + message)
print(count + str(len(guests)) + ' people')

# My dinner table won't arrive in time, I can only invite two people
print('\nSorry, everyone, but my new table won\'t arrive in time, and I can only'
      + ' invite 2 people')
apology_1 = 'Sorry, '
apology_2 = ', I don\'t have enough room to host you.'
print(apology_1 + guests.pop(0).title() + apology_2)
print(apology_1 + guests.pop(1).title() + apology_2)
print(apology_1 + guests.pop(2).title() + apology_2)
print(apology_1 + guests.pop(2).title() + apology_2)
print(count + str(len(guests)) + ' people\n')

print(guests[0].title() + ", you're still invited!")
print(guests[1].title() + ", you're still invited!")

del guests[0]
del guests[0]

print guests
