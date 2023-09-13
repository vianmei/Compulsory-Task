"""
Simple calculator application 
"""
# Add function
def add(num1 , num2)-> int:
    return num1 + num2

# Minus function 
def minus(num1 , num2)-> int:
    return num1 - num2

# Multiplication function
def multiplication(num1 , num2)-> int:
    return num1 * num2

# Division function
def division(num1 , num2)-> float:    
    return num1 / num2

# Reminder function
def reminder(num1 , num2)-> float:
    return num1 % num2

# Writefile function
def writefile(filename, value)->bool:
    file = None
    try:       
        with open(f'{filename}.txt', 'w') as file:
            file.writelines(f"{value}")
            print(f"System sucess to write the file {filename}.txt")
        return True
    except Exception as error:        
        print(error)       
        return False
    finally:
        if file is not None:
            file.close()
            return True

# Readfile function
def readfile(filename):
    file = None
    try:
                    
        with open(f'{filename}.txt', 'r') as file:
            lines = file.readlines()
            return lines           
               
    except FileNotFoundError as error:              
        return None
    except Exception as error:
        return None
    finally:
        if file is not None:
            file.close()

#Start the Program
print("Please select function as the below  : ")

is_valid = False # bool for the user input
option = 0       # define the option variable for user selected option
 
while True:
    try:
        option = input(" 1 for simple calculator , 2 for read the file : ")
        option = int(option)
        if option == 1 or option == 2:
            is_valid  = True
            break
        else:
            print (f"Sorry We can found your option : {option} .Try again...")  
                
    except Exception as error:
        print(f"Sorry We can found your option .Try again....Error: {error}")  

# User input the correct option and selected the simple calculator
if is_valid == True and  option == 1:
    
    while True:

        # Get user input numbers 
        num1 = input("Enter the first number : ")
        num2 = input("Enter the second number : ")

        total = 0
        file = None
        is_valid_num = False       
                    
        try:            
            num1 = int(num1)
            num2 = int(num2)
            is_valid_num  = True
            break;

        except ValueError as error:
            print(f"Oops! That was not a valid number. {error}")
        except Exception as error:
            print(f"Oops! That was not a valid number. {error}") 

    # If user input correct number, continue
    if is_valid_num == True:

        print ( "  1  for + addition")
        print ( "  2  for - subtraction")
        print ( "  3  for x multiplication")
        print ( "  4  for ÷ division")
        print ( "  5  for % reminder")
        option = input("Please enter the operation option : ")
        is_vaild_equation = False

        #action for operation 
        match option.strip():
            case '1':
                operation = "+" 
                total = add(num1,num2)
                is_vaild_equation = True
            case '2':
                operation = "-"  
                total = minus(num1,num2)
                is_vaild_equation = True               
            case '3':
                operation = "x" 
                total = multiplication(num1,num2)
                is_vaild_equation = True              
            case '4':
                operation = "÷"
                if num2 == 0:                                                       
                    print("Sorry, Division by zero is undefined.End the program.")                    
                else:                    
                    total = division(num1,num2)
                    is_vaild_equation = True                    
            case '5':
                operation = "%"    
                if num2 == 0:    
                    print("Sorry, Division by zero is undefined.End the program.")
                else:                    
                    total = reminder(num1,num2)
                    is_vaild_equation = True                               
            case other:                
                print("Sorry, No equation option.End the program.")
                
        if is_vaild_equation == True:
            filename = input("Your file name (If the file is not exist the system will be created the file ): ")
            input_filename = f'{filename}'   
            equation = f"{num1}  {operation} {num2} = {total}\n"
            equation_line = equation
           
            # Read the user input file
            lines = readfile(filename) 
            if lines !=None:
                for line in lines:
                    equation_line += line.strip()+"\n"

            # write the user input equation 
            is_write = writefile(input_filename, equation_line)
            if is_write == True:
                print(equation)
            else:
                print(f"System cannot create the file {filename}.txt")
   
# # User input the correct option and selected the read the file
elif is_valid == True and option == 2:
    count=0

    while True:

        read_filename = input("Your file name : ")       
        lines = readfile(read_filename)
        if lines is not None:               
            for line in lines:
                print(line.strip())
            break;
        else:
            print(f"{read_filename} file is not exist.")
        
        if count == 3:
            print("You attempt more than 3 times. End the program.")
            break;
        count +=1
                    
