'''
Task - Investigate
Use comments to answer the investigate questions on the example code.

'''
# Example Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")

# What happens if you input the guess '2'?
# Answer: it prints "Too Low!"

# What happens if you input the guess '6'?
# Answer: it prints "Too High!"

# What happens if you input the guess '5'?
# Answer: it prints "Correct!"

# What happens if you input the guess '-5'?
# Answer: it prints "Too Low!"

# What happens if you input the guess '0'?
# Answer: it prints "Too Low!"

# What do the symbols '<' and '>' mean on lines 9 and 11?
# Answer: "<" means less than and ">" means greater than

# What happens if you change line 5 to if guess = number: ?
# Answer: it would not work since "==" is conditional (checking if the values are equal) whereas "=" is a statement (stating that the values are equal)

# What do you notice about each line that FOLLOWS each IF statement?
# Answer: they are indented