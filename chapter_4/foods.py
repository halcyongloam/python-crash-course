# make a list of foods, copy it to another list, add something different to
# each one, and print both with for loops
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print('\t' + food)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print('\t' + food)
