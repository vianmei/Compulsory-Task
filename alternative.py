"""
1. Create a program called alternative.py that reads in a string and makes
each alternate character an UPPERCASE character and each other
alternate character a lowercase character (e.g, the string “Hello World”
would become “HeLlO WoRlD”).
"""

user_input = input("Enter sentence: ")
# Store new alter character
alt_user_input = ""
# Count character Modified 17-Apr-2013
len_input = len(user_input)

for x in range(len_input):
    if x % 2 == 0:   
        alt_user_input +=user_input[x].upper()
    else:
        alt_user_input +=user_input[x].lower()

# Modified 17-Apr-2013

print("1. Making each alternate character an UPPERCASE character and each other alternate character a lowercase character.")
print(alt_user_input);

"""
2. Now, try starting with the same string but making each alternative word
lower and upper case (e.g. the string: “I am learning to code” would
become “i AM learning TO code”). Using the split and join functions will
help you here
"""

# Get words list
str_list = user_input.split(" ")
# Count words
numbers = len(user_input.split(" "))

alt_sentences = []

for i in range(numbers):   
  
    if i % 2 == 0:       
        alt_sentences.append(str_list[i].lower())
    else:
        alt_sentences.append(str_list[i].upper())

print("2. Making each alternative word lower and upper case.")   
print(" ".join(alt_sentences))
