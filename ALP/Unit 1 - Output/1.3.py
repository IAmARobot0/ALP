# Task Make
# Write a program that outputs a joke on multiple lines. 
from time import *
from random import *

jokes = "why are squirrels so rich?", "how do you throw a party on the ISS?", "why did it get so hot in the stadium after the game?", "why couldn't the cs student finish his homework?", "what animal is really good at computers?"
answers = "because they eat cashews", "you planet", "because all the fans left", "he couldn't find page 404", "a RAM"

number = randint(0,4)
print(jokes[number])
print("\n\n\n")
sleep(3)
print(answers[number])