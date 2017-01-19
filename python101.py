#!/usr/bin/python

import json

# x = 100
# y = 1000
# z = 1000
# my_var = "This is a string."

#DATA TYPES
#String
x = "Lets grab dinner "
y = "and drinks"
print(x + y)

#Integer
x = 12
y = 100
z = 50

#Lists
my_list = ['one', 'two', 'three', 'four', 5]

#Dictionary
a = {'species' : 'Human', 'weight': 'too much', 'height': '72 inches'}

#JSON
my_json = json.loads('{"first_name": "Eddie", "titles": ["SE", "Systems Engineer"], "second_name": "Vedder"}')
print(my_json['first_name'])
print(my_json['titles'][1])


#PRINTING
# x = 6
# print x
# john_dinner = "pizza"
# print ("I am in the mood for " + john_dinner + " tonight.")

# stefano_dinner = "Thai"
# print "I am in the mood for " + dinner + " tonight."

# print "I personally like " , stefano_dinner

# #Printing in 2x and 3.x
# x = 6
# print (x)

# john_dinner = "Pizza"
# print ("I am in the mood for " + john_dinner + " tonight.")

# stefano_dinner = "Thai"
# print ("I am in the mood for {} tonight.".format(stefano_dinner))

# print ("I could eat {john_dinner} or {stefano_dinner} for dinner tonight.".format(john_dinner="Pizza",stefano_dinner="Thai"))






# x = 100
# y = 1000
# z = 1000
# my_var = "This is a string."

# If Statements

# if x < y:   
#  print("y is greater than x!!!")

# if True:    
# print("Today is a good day.")

# if "This" in my_var:    
# print('"This" was found in z!')

# if x > y:    print("x is greater than y!!!")

# If else Statements

# if x > y:
#    print("x is greater than y!!!")
# elif y==x:
#    print("x and y are equal!")
# elif y > z:
#    print("y is greater than z!")
# else:   
#    print("Sorry...couldn't find a good match.")



#LOOPS

# for i in range(100):
#     print(i)
    

# pets = ['dog','bird','king cobra','fish','fox','bear']
# for i in pets:
#    print("I would like to have a {} as a pet.".format(i))

# while True:
#     x+=1
#     print("We have looped {} times.".format(1+1))

# x = 1
# while x < 1000000:
#     print(x)




#Function example.
# def my_function(x):
#     print("\nmy_function was invoked with {}".format(x))
#     x = x * 100
#     return x


# b = my_function(x)
# print("b equals {}\n".format(b))


# my_num = raw_input("\nPlease enter a number to be multipled: ")

#IMPORTS
# import time
# import getpass
# import os

# If you need to pause your program to allow an auxiliary process finish completing, you can pause your code execution.

# while True:
#     time.sleep(4)
#     print("We have looped so many times....")


# login = input('Enter your username:  ')
# mypass = getpass.getpass("Please enter your get password:")

# print(mypass)

# os.system("ls -ltr")

# os.system("echo 'HI!'")





#TRY STATEMETNS

# try:
#     # y = x + z
#     y = x + my_function(int(my_num))

# except Exception as e:
#     print("\nError: {}".format(e))
    
# else:
#     print("No exception occurred.  y has an assigned value of {}".format(y))