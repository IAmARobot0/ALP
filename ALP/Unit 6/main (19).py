# Example code 1

number = 7  #assign variable number
print(
  "I have thought of a number between 1 and 10")  #outputs this string of text
guess = int(input("Can you guess what it is?")
            )  # variable guess is assigned the user's input as an integer

if guess == number:  #check if guess satisfies the condition guess = number
  print("Correct!")  #outputs "Correct!"
elif guess < number:  #compare guess and number and if guess satisfies the condition guess < number this branch is selected
  print("Too Low!")  #outputs "Too Low!"
else:  #else branch
  print("Too High!")  # out puts "Too High!"

# Example code 2

number1 = int(
  input("Please enter a number")
)  #displays prompt for user, assigns number1 to user's first input (converted to integer)
number2 = int(
  input("Please enter another number")
)  #displays prompt for user, assigns number2 to user's second input (converted to integer as well)

if number1 > number2:  #compares number1 and number2, checks if condition number1 > number2 is satisfied
  print("Number 1 is bigger than number 2")  #output if selected
elif number2 > number1:  #compares number1 and number2, checks if condition number2 > number 1 is satisfied
  print("Number 2 is bigger than number 1")  #output if selected
else:  #else branch
  print("Both numbers are the same")  #output if selected
