#write your Python code here
from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values








numbers = [] #name your list and make sure it is empty!








# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for i in range(5):
   numbers.append(randint(1,50)) # adds a random number between 1-50 to the list




search_number = max(numbers)




print(numbers)




#Count how many numbers are even and how many are odd
even_count = 0
odd_count = 0


for value in numbers:
   if value % 2 == 0:
       even_count += 1
   else:
       odd_count += 1


print("Even numbers:", even_count)
print("Odd numbers:", odd_count)


#Create a new list with unique values
unique_numbers = []


for value in numbers:
   if value not in unique_numbers:
       unique_numbers.append(value)


print("Unique numbers:", unique_numbers)


#Find the average of the numbers
numbers_sum = 0


for value in numbers:
   numbers_sum += value


average = numbers_sum / len(numbers)
print("Average value:", average)
