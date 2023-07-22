'''
Answer the questions

'''

# Example code:

names = ["Alex","Anita","Patrick","Atif","Sue"]

print("Enter a number for your choice.")
print("1. Show all")
print("2. Add name")
print("3. Show name")
print("4. Exit")
choice = int(input())

if choice == 1:
  print(names)
elif choice == 2:
  name = input("Enter the name")
  names.append(name)
elif choice == 3:
  print("Enter the index of the name")
  index = int(input())
  print(names[index])
else:
  print("Goodbye")


# What is the identifier for the list in this program?
  # Answer "names"

# What would happen if you choose option “3” and entered index “0”? 
  # Answer Atif will be printed

# What would happen if you choose option “3” and entered index “7”?
  # Answer it would not work since the index is only 0 to 4 

# What would happen if you choose option “2” and entered the name “Stuart”?
  # Answer "Stuart" would be appended to the end of the list

# What is the purpose of int(input()) on line 10 ?
  # Answer it obtains the user's choice of what they want to do

