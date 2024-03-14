# User prompted to enter three numbers and store them in variables
number_1 = int(input("Please enter a integer: "))
number_2 = int(input("Please enter another integer: "))
number_3 = int(input("Please enter a non-zero integer: "))

# number_3 cannot be 0 as it will later be a denominator so ask user to re-enter an integer
while number_3 == 0:
    number_3 = int(input("Please enter a non-zero integer: "))

# Calculate the sum of the three numbers
sum_1 = number_1 + number_2 + number_3

# Calculate the difference between the first and second number
first_minus_second = number_1 - number_2

# Calculate the product of the third and first number
third_mult_first = number_3 * number_1

# Calculate the division of the sum by the third number
sum_div_third = sum_1 / number_3

# Print the results of the calculations using formatted strings for better readability
print(f"Sum: {sum_1}")
print(f"First number minus second: {first_minus_second}")
print(f"Third number multiplied by first: {third_mult_first}")
print(f"Sum divided by third number: {sum_div_third}")
