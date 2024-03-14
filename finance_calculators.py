# importing the math library
import math 

# information on calculator types to choose from
print("""investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan""") 

# user input stored as string in 'calculator' variable
calculator = str(input("Enter either 'investment' or 'bond' from the menu above to proceed: " ))

# standardise all user inputs by capitalising all digits
calculator = calculator.upper() 


# 'if' statement for which calculator selected by user
# investment calculator
if calculator == 'INVESTMENT': 
    # all required data stored as float in variables
    depositing_money = float(input("Please enter the amount of money you are depositing: £"))
    interest_rate = float(input("Please enter the interest rate as a percentage: "))
    time_years = float(input("Please enter the number of years you plan to invest for: "))

    # interest type stored as string and standardised user input by capitalisation
    interest_type = str(input("Please enter whether you would like 'simple' or 'compound' interest applied: "))
    interest_type = interest_type.upper()

    # 'simple' interest type modelled
    if interest_type == 'SIMPLE':
        result = depositing_money * (1 + (interest_rate/100) * time_years)
        print(f"The total value of the investment after {time_years} years is: £{result:.2f}")

    # 'compound' interest type modelled
    elif interest_type == 'COMPOUND':
        result = depositing_money * math.pow((1 + (interest_rate/100)), time_years)
        print(f"The total value of the investment after {time_years} years is: £{result:.2f}")

    else:
        print("You have entered an invalid interest type, please choose 'simple' or 'compound'.")

# 'bond' calculator
elif calculator == 'BOND':
    # all required data stored as float in variables
    house_value = float(input("Please enter the value of the house: £"))
    interest_rate_year = float(input("Please enter the interest rate as a percentage: "))
    time_months = float(input("Please enter the number of months you plan to take to repay the bond: "))

    # converting yearly interest rate from percentage to decimal and monthly rate
    rate_months = (interest_rate_year/100)/12
    
    # repayment formula modelled
    repayment = (rate_months * house_value)/(1 - (1 + rate_months)**(-time_months))
    print(f"The monthly repayment for the bond is: £{repayment:.2f}")

else:
    print("You have entered an invalid calculator type, please choose 'investment' or 'bond'")