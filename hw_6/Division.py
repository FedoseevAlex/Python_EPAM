#!/usr/bin/env/ python3.6
# Task #L6.3 Exceptions

num_of_pairs = int(input('Enter number of pairs to divide:\n'))
result = list()

for num in range(num_of_pairs):
    a, b = input().strip().split(' ')
    try:
        res = str(int(a) / int(b))
    except (ValueError, ArithmeticError) as e:
        result.append('Error code: ' + str(e))
    else:
        result.append(res)
print('\n'.join(result))
