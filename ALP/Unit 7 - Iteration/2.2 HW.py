'''
Cubes Cubes Cubes
------------------

The cubed number sequence starts: 1, 8, 27, 64, 125...
Write a program that:
		 	 	 		
Asks the user to input a number.
Display N numbers in the cubed sequence according to user input. 
				
You may use any of the methods taught in class. The promt is quite brief so there is room for interpretation as to how to accomplish this task. 

'''
#Start coding below this line

number = int(input("Please enter a number: "))
for i in range(
    1, number + 1
):  #I'm not sure if the program should start printing from 0 or from 1 so I just followed the example that was given
  print(str(pow(i, 3)), end="")
  if i != number:
    print(", ", end="")
  else:
    pass
#this could be a lot more simple but I like to remove the last comma so that it looks good
