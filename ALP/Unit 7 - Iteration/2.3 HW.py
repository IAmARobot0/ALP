'''
Task - Which Room?
----------------------

Write a program that asks the user for their name and which subject they are studying.
The program should output a message telling the student by name which room to go to for that class (make up the room numbers if you need to).  You should include at least 3 subjects and have a message such as 'I don't know which room that class is in' for any you don't include.
 Example - an input of 'Ben' and 'Computing' might get an output of 'Hi Ben, go to room 401 for Computing'


You may use any method taught in class that is appropriate for this task. There is room for interpretation.

'''
#Start coding below

name = input("Enter your name: ")
subject = input("Enter your subject: ")
action = "N"
subjectlist = [("Computer Science", 100), ("Math", 101), ("English", 102),
               ("Biology", 103), ("US History", 104), ("Chemistry", 105)]

for i in range(len(subjectlist)):
  if subject == subjectlist[i][0]:
    print("Hi " + name + ", go to room " + str(subjectlist[i][1]) + " for " +
          subject)
    action = "Y"
  else:
    pass

if action == "N":
  print("I don't know which room that class is in")
else:
  pass