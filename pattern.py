# Loop through numbers from 1 to 9
for i in range(1, 10):
    # Check if the current number stored in "i" is less than or equal to 5
    if i <= 5:
        # If true, print a string of asterisks (*) equal to the current number in "i"
        print(i * "*")
    else:
        # If the number is greater than 5, calculate the difference from 10 and print
        print((10 - i) * "*")

# Can also be simplified to code without if-else statement:
# for i in range (-4,5):
#    x = 5 - abs(i)
#    print(x * "*")