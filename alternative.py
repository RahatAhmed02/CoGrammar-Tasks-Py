# Ask the user for a sentence and store it in a variable
user1_sentence = input("Please enter a sentence: ")
# Empty string variable
mod1_sentence = ""

# Loop through each character in the user input sentence
for i in range(0, len(user1_sentence)):
    # Check if the character index is even
    if i % 2 == 0:
        # If even make the character uppercase and add to the modified sentence
        mod1_sentence += user1_sentence[i].upper()
    else:
        # If odd make the character lowercase and add to the modified sentence
        mod1_sentence += user1_sentence[i].lower()

# Print the modified sentence
print(mod1_sentence)

# Split the sentence into a list of words
split2_sentence = user1_sentence.split(' ')
# Empty list to hold the modified words
mod2a_sentence = []

# Loop through each word in the list of words
for j in range(0, len(split2_sentence)):
    # Check if the word index is even
    if j % 2 == 0:
        # If even make the word lowercase and add to the list of modified words
        mod2a_sentence.append(split2_sentence[j].lower())
    else:
        # If odd make the word uppercase and add to the list of modified words
        mod2a_sentence.append(split2_sentence[j].upper())

# Join the modified words back into a single string with spaces in between
mod2b_sentence = " ".join(mod2a_sentence)

# Print the final modified sentence
print(mod2b_sentence)
