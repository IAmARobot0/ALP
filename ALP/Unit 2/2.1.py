#Predict and Run Example 1
# it will print "Andy" on the first line

firstName = "Andy"

print(firstName)

#Predict and Run Example 2
# it will print "Andy Colley" on the second line

lastName = "Colley"

fullName = firstName + " " + lastName

print(fullName)

#Predict and Run Example 3
# it will print "Hello Andy. Your full name is Andy Colley."

print("Hello " + firstName + ". Your full name is " + fullName + ".")

print(firstName, lastName + "") # alternative way to print full name
print(len(firstName))
for i in range(len(firstName)):
  print(firstName[i] + " ", end="")
print("\n")
for j in range(len(fullName)):
  print(fullName[j] + " ", end="")