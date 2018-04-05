# print the numbers from 1 to 1 million
nums = []
for num in range(1, 1000001):
    nums.append(num)
    print(num)

# print the sum, minimum, and maximum numbers in the list
print('The first number is ' + str(min(nums)))
print('The last number is ' + str(max(nums)))
print('The sum of the first one million integers is ' + str(sum(nums)))
