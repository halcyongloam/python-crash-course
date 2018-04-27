# write ten conditional tests on various things

food = 'Bacon'
print("Does food == 'bacon'? I predict True")
print(food.lower() == 'bacon')

print("\nDoes food == 'anchovies'? I predict False")
print(food == 'anchovies')

print("\nDoes food != 'Bacon? I predict False")
print(food != 'Bacon')

n = 10
print("\nDoes n == 10? I predict True")
print(n == 10)

print("\nIs n > 10 and n < 20? I predict False")
print(n > 10 and n < 20)

print("\nIs n <= 10 or n >= 20? I predict True")
print(n <= 10 or n >= 20)

toppings = ['sausage', 'bacon', 'cheese']
print("\nIs 'cheese' in toppings? I predict True")
print('cheese' in toppings)

print("\nIs 'anchovies' in toppings? I predict False")
print('anchovies' in toppings)

print("\nIs 'bacon' not in toppings? I predict False")
print('bacon' not in toppings)

print("\nIs 'olives' not in toppings? I predict True")
print('olives' not in toppings)
