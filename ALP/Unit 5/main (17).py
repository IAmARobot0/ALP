# Starter Code

number = 5 # assigns variable number to 5
print("I have thought of a number between 1 and 10") # outputs directions for the user
guess = int(input("Can you guess what it is?")) # takes the user's input and converts it into an integer


if guess < number: # test to see if the condition guess < number is satisfied
  print("Too Low!") # if this branch is selected, the program will print "Too Low!"
if guess > number: # test to see if the condition guess > number is satisfied
  print("Too High!") # if this branch is selected, the program will print "Too High!"

