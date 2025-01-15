# Using loop and the range function add all even numbers from 0 to 100
Sum_Even_numbers = 0
for num in range(0, 101, 2):
    """ Sum_Even_numbers += num
    print(Sum_Even_numbers) """
    if num % 2 == 0:
        Sum_Even_numbers += num

print(Sum_Even_numbers)