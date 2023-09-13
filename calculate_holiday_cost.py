"""
Your task will be to
calculate a user’s holiday cost including the plane cost, hotel cost, and
car rental cost.
"""
# The daily car rental cost 
daily_rental_cost = 50.00
# The price per night charged at the hotel
price_per_night = 100.00

# Plane cost list [ id , city, plane cost ]
plane_cost_data = [[1, "New York ,USA", 300.00],
                   [2, "London , England", 200.00],
                   [3, "Hong Kong", 500.00],
                   [4, "St Johns, Canada", 400.00],
                   [5, "Auckland , New Zealand", 700.00]]


# Get the plane cost from the plane_cost_data
def plane_cost(city_id):
    cost = 0
    for plane in plane_cost_data:
        if city_id == plane[0]:
            cost = plane[2]
    return cost


# Calculate the total cost for the hotel stay
def hotel_cost(nights):
    return nights * price_per_night


# Calculate the total cost of the car rental
def car_rental(days):
    return days * daily_rental_cost


# Calculate the total cost of holiday
def holiday_cost(plane, hotel, car):
    return plane + hotel + car


# Get the destination from the plane_cost_data
def get_destination(city_id):
    city_name = None
    for plane in plane_cost_data:
        if city_id == plane[0]:
            return plane[1]
    return city_name


# City Flight Option
def city_options():
    print("City Flight Options:")
    print("1 = New York ,USA")
    print("2 = London")
    print("3 = Hong Kong")
    print("4 = St Johns, Canada")
    print("5 = Auckland, New Zealand")


# Holiday function Option
def holiday_function_options():
    print("0 = All")
    print("1 = Plane cost")
    print("2 = Hotel cost")
    print("3 = Car Rental cost")


# Dictionary : Value it maps to function
get_holiday_function = {
    '1': plane_cost,
    '2': hotel_cost,
    '3': car_rental,
}

# Define variable
city = ""
city_flight = 0
num_nights = 0
rental_days = 0
plane_fee = 0
hotel_fee = 0
car_rental_fee = 0
total_cost = 0
function_list = []  # Store user choose function

# Start the program
print("--- Calculate the Holiday Cost ---")
print("Which cost would you like to calculate?")
# Show user calculate cost functions
holiday_function_options()
print("If you choose the multi-option, you should be separated by a comma e.g. 1,2,3 ")
user_options = input("Which function you will use : ")

try:
    function_list = user_options.split(",")
except Exception as error:
    print(f"Sorry We cannot calculate your holiday cost .Error: {error}")

if len(function_list) > 0:

    for choice in function_list:
        choice = choice.strip()
        # Get plane , hotel and car rental cost
        if choice == '0':

            try:
                city_options()
                city_flight = input("Which city you will be flying (Input the option as above): ")
                num_nights = input("Number of nights you will be staying at a hotel: ")
                rental_days = input("Number of days that they will be hiring a car for: ")

                city_flight = int(city_flight)
                num_nights = int(num_nights)
                rental_days = int(rental_days)

                # get city name
                city = get_destination(city_flight)

                # get plane , hotel and car rental cost
                plane_fee = plane_cost(city_flight)
                hotel_fee = hotel_cost(num_nights)
                car_rental_fee = car_rental(rental_days)

            except Exception as error:
                print(f"Sorry We cannot calculate your holiday cost .Error: {error}")
                break

            break
        # Get plane cost
        elif choice == '1':
            city_options()
            city_flight = input("Which city you will be flying (Input the option as above): ")

            try:
                city_flight = int(city_flight)
                # get city name
                city = get_destination(city_flight)
                plane_fee = get_holiday_function[choice](city_flight)
            except Exception as error:
                print(f"Sorry We cannot calculate your plane cost .Error: {error}")
                break
        # Get hotel cost
        elif choice == '2':
            try:
                num_nights = input("Number of nights you will be staying at a hotel: ")
                num_nights = int(num_nights)
                hotel_fee = get_holiday_function[choice](num_nights)
            except Exception as error:
                print(f"Sorry We cannot calculate your hotel cost .Error: {error}")
                break
        # Get car rental cost
        elif choice == '3':
            try:
                rental_days = input("Number of days that they will be hiring a car for: ")
                rental_days = int(rental_days)
                car_rental_fee = get_holiday_function[choice](rental_days)
            except Exception as error:
                print(f"Sorry We cannot calculate your car rental cost .Error: {error}")
                break
        else:
            print(f"We have no this option {choice}")

    if plane_fee != 0 or hotel_fee != 0 or car_rental_fee != 0:
        if plane_fee > 0:
            print(f"--- City Flight ---")
            print(f"City : {city}")
            print(f"Plane cost : £{plane_fee:.2f}")

        if hotel_fee > 0:
            print(f"--- Hotel ---")
            print(f"Price per nights : £{price_per_night:.2f}")
            print(f"Number of nights : {num_nights}")
            print(f"Hotel cost : £{price_per_night:.2f} x {num_nights} nights = £{hotel_fee:.2f}")

        if car_rental_fee > 0:
            print(f"--- Car Rental ---")
            print(f"Daily Rental Cost : £{daily_rental_cost:.2f}")
            print(f"Number of rental_days : {rental_days}")
            print(f"Car Rental cost : £{daily_rental_cost:.2f} x {rental_days} nights = £{car_rental_fee:.2f}")

        # Calculate Holiday fee
        total_cost = holiday_cost(plane_fee, hotel_fee, car_rental_fee)
        # Print out all the details about the holiday
        print(f"--- Holiday Cost ---")
        print(f"The total cost for your Holiday : ")
        print(f"Plane cost : £{plane_fee:.2f}  + Hotel cost :£{hotel_fee:.2f} + Car Rental :£{car_rental_fee:.2f}")
        print(f"Holiday Cost is £{total_cost:.2f}")

    else:
        print(f"Sorry We cannot calculate your holiday cost .")

else:
    print(f"Sorry We cannot calculate your holiday cost .")
