# Example code 1

# Add comments to each line to say whether it is inside or outside the loop and what it does.

# Explain the circumstances in which the loop will run.

print("What is the capital of France?")  #prints prompt
answer = input()  #asks for input from the user, string

while answer != "Paris":  #loop runs when answer is not "Paris"
  print("Incorrect! Try again."
        )  #inside loop, prints the response to an incorrect answer
  answer = input("What is the capital of France?"
                 )  #inside the loop, asks for new input from the user, string

#answer is "Paris" so the loop stops
print("Correct!")  #final answer

# Example code 2

counter = 1  #original variable counter

while counter < 5:  #loop runs when counter is less than 5
  print("This code is inside the loop")  #inside the loop, prints that as well
  counter += 1  #counter increases by 1

#kicks out of loop when counter is 5, running 4 times total