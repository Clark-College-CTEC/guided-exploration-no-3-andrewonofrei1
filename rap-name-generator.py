# Guided Exploration No. 3
# Andrew Onofrei

import random  # this allows for the code to have access to the random library.

possible_names = []  # this creates an empty list for us to add to.

# this creates a text file where we will be putting the rap name(s)
outputFile = open('rap-names-output.txt', 'w')
with open('rap-names.txt', 'r') as dataFile:
    for name in dataFile:
        possible_names.append(name.rstrip())
# this (lines10-12) asks for user input for how many rap names they'd like
count = int(input('How many rap names would you like to create? '))
# this asks how many parts ot the name they want in the names
parts = int(input('How many parts should the name contain? '))
for i in range(count):  # this for loop repeats itself depending on what number the user used for the variable count
    name_parts = []  # this created another empty list for the loop
    for j in range(parts):  # another loop, which is dependent on the user's second number, which they assigned to the variable parts
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])  # this code, inlcuding the line above it, is taking the number that was assigned, which is how many times they'll go through the process. Then it goes through, and from the list of rap-names.txt, it chooses random elements to create the rap name.
# this code takes the string, name_parts, and writes it inside the text file outputFile
outputFile.write(f"{' '.join(name_parts)}\n")
# this code then prints out that string, inside the text file, for the user to see.
print(f"{' '.join(name_parts)}")
outputFile.close()  # this closes the program
