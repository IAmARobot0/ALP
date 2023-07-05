'''
In the modify tasks, you are given some starter code.
Use the instructions below to make changes to the code.
Comment your changes to explain what you have done.

Adapt the code to:
- Rename the function so that it has a sensible name. Don't forget to rename it when it is called.
- Call the function with the argument 'Sweden'.
- Get the user to input a country. Store it in a variable. Call the function again with the variable as the parameter.
'''


def i_am_from(country):
  print("I am from " + country)


i_am_from("Brazil")
i_am_from("Sweden")
usercountry = input("Where are you from?\n")
i_am_from(usercountry)
