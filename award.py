# Prompt the user to enter their swimming time in minutes and store it as an integer in 'swimming'
# Prompt the user to enter their cycling time in minutes and store it as an integer in 'cycling'
# Prompt the user to enter their running time in minutes and store it as an integer in 'running'

# Calculate the sum of 'swimming', 'cycling', and 'running' and store it in 'final_time'

# Check if 'final_time' is greater than 0 and less than or equal to 100
# If true, print "Provincial Colours."

# If 'final_time' is not in the range of 0 to 100, check if it's in the range of 101 to 105.
# If true, print "Provincial Half Colours."

# If 'final_time' is not in the range of 101 to 105, check if it's in the range of 106 to 110
# If true, print "Provincial Scroll."

# If none of the above conditions are met, print "No award."

swimming = int(input("Please enter your swimming time in minutes: "))

cycling = int(input("Please enter your cycling time in minutes: "))

running = int(input("Please enter your running time in minutes: "))

final_time = swimming + cycling + running

if 0 < final_time <= 100:
    print("Provincial Colours")

elif 101 < final_time <= 105:
    print("Provincial Half Colours")

elif 106 < final_time <= 110:
    print("Provincial Scroll")

else:
    print("No award")
