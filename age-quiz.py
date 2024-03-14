# Prompt the user to enter their age as an integer and store it in the variable 'age'
# Check if 'age' is greater than 100, if true, print "Sorry, you're dead."
# If 'age' is not greater than 100, check if it's greater than or equal to 65, if true, print "Enjoy your retirement!"
# If 'age' is not greater than or equal to 65, check if it's greater than or equal to 40, if true, print "You're over the hill."
# If 'age' is not greater than or equal to 40, check if it's less than 13, if true, print "You qualify for the kiddie discount."
# If 'age' is not less than 13, check if it's equal to 21, if true, print "Congrats on your 21st!"
# If none of the above conditions are met, print "Age is but a number."

age = int(input("Please enter your age: "))

if age > 100:
    print("Sorry, you're dead.")

elif age >= 65:
    print("Enjoy your retirement!")

elif age >= 40:
    print("You're over the hill.")

elif age < 13:
    print("You qualify for the kiddie discount.")

elif age == 21:
    print("Congrats on your 21st!")

else:
    print("Age is but a number.")