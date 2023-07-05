# Example Code 1


def say_hi():  #defines subrountine
  print("Why hello there!")  #when called it will print


def offer_drink():  #defines subrountine
  print("Would you care for a spot of tea?")  #when called it will print


def offer_food():  #defines subrountine
  print("Biscuit?")  #when called it will print


def say_bye():  #defines subrountine
  print("Cheerio then.")  #when called it will print


offer_drink(
)  #calls the offer_drink() function, which prints "Would you care for a spot of tea?"
say_hi()  #calls the say_hi() function, which prints "Why hello there!"
offer_food()  #calls the offer_food() function, which prints "Biscuit?"


# Example code 2
def maths1():  #defines function
  num1 = 50  #variable assigned
  num2 = 5  #variable assigned
  return num1 + num2  #returns the result


def maths2():  #defines function
  num1 = 50  #variable assigned
  num2 = 5  #variable assigned
  return num1 - num2  #returns the result


def maths3():  #defines function
  num1 = 50  #variable assigned
  num2 = 5  #variable assigned
  return num1 * num2  #returns the result


outputNum = maths2(
)  #the result that maths2 returns is assigned to variable outputNum
print(outputNum)  #prints outputNum


# Example Code 3
def location(country):  #defines subrountine
  print("I am from " + country)  #when called it will print


location(
  "Brazil")  #calls the location() function, which prints "I am from Brazil?"
