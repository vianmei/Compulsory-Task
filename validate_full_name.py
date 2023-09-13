"""
This is program will be used to validate that a user inputs at least two names when asked to enter their full name
"""

# function for asking the user to input their full name#
def input_user_full_name():
    name = input("Your name : ")
    surname = input("Your surname : ")
    check_user_name(name, surname)


# validate the user full name function
def check_user_name(name, surname):

    full_name = name + surname

    #Get the full name length
    leng_of_name = len(full_name)

    #Condition
    if leng_of_name == 0:
        print("you haven't entered anything. Please enter your full name.")
        input_user_full_name()
    elif (leng_of_name < 4) and (leng_of_name > 0):
        print("You have entered less than 4 characters. Please entered your name and surname.")
        input_user_full_name()
    elif leng_of_name > 25:
        print("you have entered more than 25 characters. Please make sure that you have only entered your full name")
        input_user_full_name()

    else:
        full_name = name + " " + surname
        print("Thank you for entering your name : " + full_name)


# Start the program
print("Please input your full name")
input_user_full_name();
