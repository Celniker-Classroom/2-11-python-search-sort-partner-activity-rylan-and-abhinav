#write your python code here
from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values

numbers = [] #name your list and make sure it is empty!

# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for i in range(5): #for loop appends 5 numbers to your list, but make sure you name your variable
    numbers.append(randint(1,50)) #this adds a random number between 1-50 to the list

search_number = int(input("Enter a number:")) 

print(numbers) #print the list!

if search_number in numbers:
    print("Number",search_number,"found in the list!")
else:
    print("Number",search_number,"not found in the list.")


comparisons = 0  # Initialize the counter for comparisons
found = False  # Variable to track if the number was found


for i in numbers:  # Name your variable in the for loop
    comparisons += 1  # Increment the counter for each comparison
    if i == search_number:
        found = True  # Set found to True if the number is in the list
        break  # Exit the loop early if the number is found

if found == False:
    print("Number not found after",comparisons,"comparisons.")
else:
    print("Number found after",comparisons,"comparisons.")
