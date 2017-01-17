#!/usr/bin/python3



x = 100
y = 1000
z = 1000
my_var = "This is a string."

#if statements

#if x < y:
#     print("y is greater than x!!!")

#if True:
#     print("Today is a good day.")

#if "This" in z:
#     print('"This" was found in z!')

#more if statements
# if x > y:
#    print("x is greater than y!!!")

# elif y==x:
#    print("x and y are equal!")
# elif y > z:
#    print("y is greater than z!")
# else:
#    print("Sorry...couldn't find a good match.")


#Function example.  Passed by value vs reference.
def my_function(x):
    x = x * 100
    print(x)
    return x

# b = my_function(x)
# print("b equals {}".format(b))
# #Who wants to win a prize?  What will the following line print?
# print(x)

# b = my_function(x)
# print("b equals {}".format(b))


my_name = eval(input("What is your name?"))
print(my_name)
