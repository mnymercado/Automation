# Compute the sum of digits in all numbers from 1 to n.
# When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15


def sum_of_all_num(n):
    sum_result = 0
    while n > 0:
        sum_result += n
        n -= 1
    print(sum_result)


sum_of_all_num(5)


#-------------------------------------------------------------------------
# Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.

value_1 = 124
value_2 = 21
value_3 = 32


if value_1 > value_2 and value_1 > value_3:
    result = value_1
elif value_2 > value_1 and value_2 > value_3:
    result = value_2
else:
    result = value_3

# print(result)



#-------------------------------------------------------------------------
# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

number = str(34560)

odd_list = []
even_list = []

for x in number:

    if int(x) % 2 == 0:
        even_list.append(int(x))
    else:
        odd_list.append(int(x))

# print('Odd: ', odd_list)
# print('Even: ', even_list)


