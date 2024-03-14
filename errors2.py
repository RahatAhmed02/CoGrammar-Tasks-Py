# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # Runtime error: String needs to be enclosed in quotations, Python mistakens it for a variable therefore runtime error
animal_type = "cat" # Logical error: Lion is a cat, cub is a life stage of a lion
number_of_teeth = 16 # Possible logical error, lions typically have 30 teeth

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth." # Logical error: Missing "f" at beginning so prints variable name instead, variables animal_type and number_of_teeth wrong way round

print (full_spec) # Syntax error: variable needs to be enclosed in parantheses