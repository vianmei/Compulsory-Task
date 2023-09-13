"""
Write a program that always asks the user to enter a number.
When the user enters - 1, the program should stop requesting the user to  enter a number
The program must then calculate the average of the numbers entered,
excluding the -1.
"""

count = 0  # Count the user input
total = 0  # sum of the user input number
num = 0  # user input number
avg_num = 0  # average of the numbers

while num != -1:
    try:
        num = int(input("Please enter the number : "))
        if num != -1:
            total += num
            count += 1

    except ValueError as valueError:
        print("Oops! That was not a valid number. Try again...")
    except Exception as exception:
        print(exception)

if count > 0:
    avg_num = total / count
    print(f'The average of the numbers : {avg_num}')
else:
    print(f'The average of the numbers : ')
