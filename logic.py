# Program to calculate new bank balance after applying annual interest

initial_balance = 1000  # Initial bank balance in pound sterling, the initial balance is £1000

interest_rate = 5  # The annual interest rate is 5%

new_balance = initial_balance * interest_rate / 100 # Calculate new balance with interest
# Logical Error: Interest calculation is incorrect. It does not add the additional money on to intial_balance

# Print the result
print(f"""Thank you for banking with NatWest, 
Your new balance for this year after applying last years interest is: £{new_balance}""")