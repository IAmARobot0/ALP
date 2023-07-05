# Starter Code

number1 = int(input("Please enter a number"))
number2 = int(input("Please enter another number"))
number3 = int(input("Please enter another number"))

if number1 > number2:
  print("Number 1 is bigger than number 2")
elif number2 > number1:
  print("Number 2 is bigger than number 1")
else:
  print("Both numbers are the same")

if number1 > number3:
  print("Number 1 is bigger than number 3")
elif number3 > number1:
  print("Number 3 is bigger than number 1")
else:
  print("Both numbers are the same")

if number2 > number3:
  print("Number 2 is bigger than number 3")
elif number3 > number2:
  print("Number 3 is bigger than number 2")
else:
  print("Both numbers are the same")

#Alternative way using tuples!!!!
n1 = input("Please enter a number")
n2 = input("Please enter another number")
n3 = input("Please enter another number")

list1 = [('number 1', n1), ('number 2', n2), ('number 3', n3)]


def sort_key(list1):
  return list1[1]


list1.sort(key=sort_key, reverse=False)

print(str(list1[1][0]) + " is bigger than " + str(list1[0][0]))
print(str(list1[2][0]) + " is bigger than " + str(list1[0][0]))
print(str(list1[2][0]) + " is bigger than " + str(list1[1][0]))