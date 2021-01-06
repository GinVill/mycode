#!/usr/bin/env python3

# super clunky to require script to run in order to get file name
# in real world, input would also need to be validated
fileName = input("What is the name of the file to load?")

## create file object in "r"ead mode
with open(fileName, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

