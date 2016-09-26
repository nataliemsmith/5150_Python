######################################################
#   MIS 5150
#   Module 1.3 Homework
#   Natalie Smith
######################################################
#exercise 1
print ("------Begin Exercise 1------")
width = 17
height = 12.0

x = width / 2
print (x)
print (type(x))

y = width / 2.0
print (y)
print (type(y))

z = height/3
print (z)
print (type(z))

a = 1 + 2 * 5
print (a)
print (type(a))


#exercise 2
print ("------Begin Exercise 2------")
meal = 44.50
tax = .0675
tip = .15

meal = meal + (meal * tax)
print (meal)

total = meal + (meal * tip)
print (total)
print("%2.2f" % total)


#exercise 3
print ("------Begin Exercise 3------")
my_string = "hello world"
print (len(my_string))
print (my_string.upper())


#exercise 4
print ("------Begin Exercise 4------")
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
print ("Pay: " + str(hours * rate))


import time
#exercise 5
print ("------Begin Exercise 5------")
print (time.strftime("%m/%d/%Y %H:%M:%S"))


#exercise 6
print ("------Begin Exercise 6------")
celsius = int(input("Enter a temperature in Celsius: "))
fahrenheit = print("Fahrenheit: " + str((celsius * (9 /5 )) + 32))

