score = int(input("Enter your test score: "))
fail = "N"
grade = "U"
if score > 100:
  print("Above and beyond! You got over 100!")
elif score < 1:
  print("How did this happen...")
else:
  #check grade
  if score >= 80:
    grade = "A"
  elif score >= 69:
    grade = "B"
  elif score >= 40:
    grade = "C"
  elif score < 40:
    grade = "U"
    fail = "Y"
  else:
    pass

  #check fail
  if fail != "N":
    print("Retake required")
  else:
    print("Passed")

  #grammar
  if grade == "A":
    print("You got an '" + grade + "' grade.")
  else:
    print("You got a '" + grade + "' grade.")


'''
i hope this is a good explanation
if score fails to satisfy the first if statement, score is not greater than or equal to 80, so it must be less than 80. python will then go down and check the next if statement. python knows that score failed the previous if statement (meaning score < 80) and python will check if score >= 69, so python will be checking the range 69 to 79.

extra notes:
this works becasue python reads from top to bottom, so it reads the first if statement before going to the next line.
score is an integer. this means that the max of the second if statement will be 79 not 79.xx (integers cant have decimals).
  '''