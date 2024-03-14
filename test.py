# User prompt to enter a number and store it in user_number
user_number = float(input("Please enter a number: "))
entries = 0
total = 0

# While loop that continues as long as the user does not enter -1
while user_number != -1:
    # Add the current value of user_number to the total
    total += user_number
        # Increment the number of valid entries
    entries += 1
    # User prompt to enter another number and store it in user_number
    user_number = float(input("Enter another number number: "))

# Check for any valid entries
if entries > 0:
    # Calculate and print the average of the entered numbers if valid entries
    average = total/entries
    print(f"Average of values entered is: {average}")
else:
    # If there were no valid entries, print a message indicating so
    print("No valid numbers entered")

