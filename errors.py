# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # Syntax error: Forgot the parantheses
print ("\n") # Syntax error: Unexpected indentation and paratheses missing

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" # Syntax error: Unexpected indentation, Runtime error: The variable was not defined before its use correctly "==" (NameError), also variable needs to be made concise only numerical string since will be converted to integer later
age = int(age_Str) # Syntax error: Unexpected indentation
print("I'm " + age_Str + " years old.") # Syntax error: Unexpected indentation, Runtime error: Cannot concatenate string and integer, need to use age_Str variable (TypeError)

# Variables declaring additional years and printing the total years of age
years_from_now = 3.5 # Syntax error: Unexpected indentation, Runtime error: Variable needs to store numerical value as integer for its use case (TypeError), Logical error: Should be 3.5 years since the hint tells us the answer is 330 months which also coincides with last print statement of 3 years and 6 months
total_years = age + years_from_now # Syntax error: Unexpected indentation

print ("The total number of years: " + str(total_years)) # Syntax error: Forgot the parantheses, Runtime error: There is no defined variable 'answer_years', meant to be 'str(total_years)' Logical error: Unintended result because originally variable 'answer_years' was in quotations but we want the contents of the variable not the label

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 # Runtime error: Undefined variable orginally used (NameError)
print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # Syntax error: Forgot the parantheses, Runtime error: Cannot concatenate string and integer, needs to be converted first (TypeError)


#HINT, 330 months is the correct answer
