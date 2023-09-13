"""
Determines the award a person competing in a
triathlon will receive.
"""
# Parameter
swimming_time = 0
cycling_time = 0
running_time = 0
total_time = 0  # Triathlon time
participant = ""
qualifying_time = 100  # Within qualifying time
qualifying_time_add_five = qualifying_time + 5  # Within 5 minutes of qualifying time.
qualifying_time_add_ten = qualifying_time + 10  # Within 10 minutes of qualifying time.


# Check empty value function
def check_empty(value):
    length_of_value = len(value)
    if length_of_value > 0:
        return True
    else:
        print(f"The value is empty.")
        return False


# Determine the award function
# parameter time : integer
def award(time):
    if 0 < time <= qualifying_time:
        print("Your Award : Provincial Colours")
    elif qualifying_time < time <= qualifying_time_add_five:
        print("Your Award : Provincial Half Colours")
    elif qualifying_time_add_five < time <= qualifying_time_add_ten:
        print("Your Award : Provincial Scroll")
    elif time > qualifying_time_add_ten:
        print("Sorry you have no award.")
    else:
        print("Sorry you have no award.")


# Get participant's name from input command
def get_user_name():
    name = input("Enter Participant Name : ")
    if name is None:
        print(f"The Participant Name is empty.")
        return None
    else:
        return name


# Get event time from input command
# parameter event : string
# return time : integer
def get_event_time(event):
    while True:
        time = input("Enter " + event + " records (in minutes) : ")
        if check_empty(time):
            try:
                time = int(time)
                return time
                break;
            except:
                print("The enter value is not number.")
                continue;
        else:
            return -1
            break;


# Print event records
# parameter event : string
# parameter time : integer
def print_msg(event, value):
    if value == -1:
        return "You " + event + " event have no record"
    else:
        return event + " event : " + str(value) + " minutes"


# Start the program
print("Please input triathlon records")
participant = get_user_name()
swimming_time = get_event_time("Swimming")
cycling_time = get_event_time("Cycling")
running_time = get_event_time("Running")

# Calculate the triathlon time
# If your finished three event , then display the result and award
if swimming_time > 0 and cycling_time > 0 and running_time > 0:

    total_time = swimming_time + cycling_time + running_time

    # print the award a person competing
    print("")
    print(participant + " Triathion Records : ")
    print(print_msg("Swimming", swimming_time))
    print(print_msg("Cycling", cycling_time))
    print(print_msg("Running", running_time))
    print("Your Triathlon Time : " + str(total_time) + " minutes")
    award(total_time)

else:

    print("")
    print(participant + " Triathion Records : ")
    print(print_msg("Swimming", swimming_time))
    print(print_msg("Cycling", cycling_time))
    print(print_msg("Running", running_time))
    print("Sorry " + participant + ". You have no award.")

