# User prompt to enter a sentence and store it in the variable str_manip
str_manip = input("Please enter a sentence: ")

# Print the length of the entered sentence
print(f"The length of the sentence is: {len(str_manip)}")

# Get the last letter of the entered sentence
last_letter = str_manip[-1]

# Replace all occurrences of the last letter in the sentence with '@'
replace = str_manip.replace(last_letter, "@")

# Print the modified sentence with replaced characters using formatted string
print(f"The character replaced sentence is: {replace}")

# Extract the last three characters of the sentence in reverse
three_backwards = str_manip[:-4:-1]

# Print the last three characters in reverse using formatted string
print(f"The last three letters backwards is: {three_backwards}")

# Extract the first three characters of the sentence
first_three = str_manip[0:3]

# Extract the last two characters of the sentence
last_two = str_manip[-2:]

# Concatenate the first three and last two characters to form a new word
five_letter_word = first_three + last_two

# Print the new five-letter word using formatted string
print(f"Your new word is: {five_letter_word}")
