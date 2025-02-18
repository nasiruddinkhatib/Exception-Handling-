#Exception handling in Python is done using the try, except, else, and finally blocks. Here's a breakdown of each:
# try block: Contains code that might raise an exception.
# except block: Catches and handles exceptions that occur in the try block.
# else block: Executes if no exception occurs in the try block.
# finally block: Executes no matter what (whether an exception occurs or not), and is typically used for clean-up actions.
# Why Use Exception Handling?
# When writing code, things can sometimes go wrong — like dividing by zero, accessing a file that doesn('t exist, or receiving unexpected input.'
#  In such cases, Python raises exceptions to indicate that something went wrong.Without proper handling, your program will crash.
# Exception handling lets you manage these errors gracefully instead of the program terminating unexpectedly.)

#**************-----------*****************----------------*****************------------------****************---------------************
##Example:
#The try block will generate an error, because x is not defined:
# try:
#   print(x)
# except:
#   print("An exception occurred")
#**************--------------***************-------------------------*******************-------------------------***********************
##Example 2*********Division By Zero Error******************
try:
    num = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division was successful!")
finally:
    print("This always executes.")

#***********
