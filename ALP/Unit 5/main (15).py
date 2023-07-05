'''
Task - Predict and Run
This task contains three code examples.

Look at each example , study it carefully. Write a prediction of what it will do when it runs. Your prediction should be added to the code as comments. You should use the key terms selection, condition and branch in your prediction.
'''

# Example code 1

age = 18

if age > 18:  # the condition is that age > 18
  print("You are old enough to drive"
        )  # when the selection is made, the print statement is performed

# Example code 2

num1 = 1337

# there are 2 branches, the if branch and the else branch
if num1 == 10:  # branch 1, the condition is that num1 = 10
  print("This text is output because the condition was true"
        )  # when the selection is made, the print statement is performed
else:  # branch 2, the condition is that the if statement is not followed
  print("This text is output because the condition was false")

# Example code 3

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?")
            )  # collects the user's data and turns it into an integer

# not multiple branches here since they are all individual if statements
if guess == number:  # condition is guess = number
  print("Correct!") # when the selection is made, the print statement is performed
if guess < number:  # condition is guess < number
  print("Too Low!") # when the selection is made, the print statement is performed
if guess > number:  # condition is guess > number
  print("Too High!") # when the selection is made, the print statement is performed
