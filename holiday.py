# Define function that outputs hotel cost
def hotel_cost(num_nights):
    # Assuming the cost per night is $120
    return num_nights * 120

# Define function that outputs flight cost
def plane_cost(city_flight):
    # Fixed flight costs for a set of cities
    flight_costs = {
        'LONDON': 400,
        'PARIS': 350,
        'NEW YORK': 600,
        'ROME': 250,
        'LOS ANGELES': 650,
        'MADRID': 300,
    }

    # Standardise sentence case of user input
    city_flight = city_flight.upper()
    # Use if/else to return a cost or 'None' if destination not available
    if city_flight in flight_costs:
        return flight_costs[city_flight]
    else:
        return None

# Define function that outputs car rental cost    
def car_rental(rental_days):
    # Assuming the cost per day for renting a car is $40
    return rental_days * 40

# Define function that outputs total cost of holiday
def holiday_cost(city_flight, num_nights, rental_days):
    # Calculate the total cost, initialise total_cost
    total_cost = 0
    
    if plane_cost(city_flight) is not None:
        total_cost += plane_cost(city_flight)
    else:
        print("Invalid flight destination")
    
    total_cost += hotel_cost(num_nights)
    
    total_cost += car_rental(rental_days)
    
    return total_cost

# Get user inputs with error handling
city_flight = input("We fly to London, Paris, New York, Rome, Los Angeles, Madrid. Enter the city you are flying to: ")

try:
    num_nights = int(input("Enter the number of nights you'll stay at the hotel: "))
    if num_nights <= 0:
        raise ValueError
except ValueError:
    print("Invalid input for hotel nights, please enter a positive whole number.")

try:
    rental_days = int(input("Enter the number of days you will rent a car: "))
    if rental_days <= 0:
        raise ValueError
except ValueError:
    print("Invalid input for car rental days, please enter a positive whole number.")

# Calculate and print the holiday cost
total_cost = holiday_cost(city_flight, num_nights, rental_days)

# Filter valid flights from invalid 
# If invalid, no result whatsoever printed until valid destination entered
if plane_cost(city_flight) == None:
    print("Please enter a valid destination.")
else:
    print(f"""
    To fly to {(city_flight.lower()).capitalize()} and stay in a hotel for {num_nights} nights,
    and to rent a car for {rental_days} days, your cost comes to:

    Total cost: ${total_cost}
    Flight cost: ${plane_cost(city_flight)}
    Hotel cost: ${hotel_cost(num_nights)}
    Car cost: ${car_rental(rental_days)}
    """)
