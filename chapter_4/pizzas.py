# store a list of pizzas, do a for loop with it
pizzas = ['bacon', 'chicken', 'sausage']
# copy my favorite pizzas into a for loop, then add a different pizza to each
friend_pizzas = pizzas[:]

pizzas.append('gorgonzola pesto')
friend_pizzas.append('anchovy')

# print each list with a for loop to prove that it's distinct
for pizza in pizzas:
    print('I like ' + pizza + ' pizza.')

print('\n')

for pizza in friend_pizzas:
    print('My friend likes ' + pizza + ' pizza.')

print('\nAs you can see, I have much better tast than my friend.')
