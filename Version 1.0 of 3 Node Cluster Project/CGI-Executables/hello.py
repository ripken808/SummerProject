#!/usr/bin/python3
#!- - - - - - - - - -!#

#TODO Import libraries needed for code.
# ? Imports date in order to find out what date it is.
from datetime import date
#!- - - - - - - - - -!#

#TODO Makes sure that the python code can be executed as an html file.
# ? Allows my python code to execute as an html file.
print ("Content-type: text/html\n\n")
#!- - - - - - - - - -!#

#TODO Print out a string that includes todays date.
# ? Creates a variable to save the date and prints out 
# ? prints out a string including the date onto the website
today = date.today()
print("Hello World!\t" + "Today's Date:", today)
