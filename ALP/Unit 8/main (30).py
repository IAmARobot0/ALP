'''
Reference Link
https://docs.google.com/document/d/1Lf221krWqB0vv5zSaQDvzBi6you6AuKdfn5x1TETh7Q/edit?usp=sharing
'''
'''In the modify tasks, you are given some starter code.
Use the instructions below to make changes to the code.
Comment your changes to explain what you have done.

Adapt the code to:

1- Add 'Minecraft' to the start of the list.

2- Ask the user to input a number between 0 and 4 and store it in a variable.  Output the item at this position in the list.

3- Ask the user to input the name of a video game and store it in a variable.  
  3.1- If this video game is in the list then remove it from the list.
  3.2- If it isn't in the list then add it to the end.
'''

# Starter Code

videoGames = ["Mario", "Sonic", "Joust", "Zelda"]
videoGames.insert(0, "Minecraft")
number = int(input("Please input a number between 0 and 4: "))
print(videoGames[number])
name = input("Please input a video game name: ")
action = "n"
for i in range(4):
  if name == videoGames[i]:
    videoGames.pop(i)
    i = 5
    action = "y"
  else:
    pass

if action == "n":
  videoGames.append(name)
else:
  pass

print(videoGames)
