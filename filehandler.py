"""
Version 1: raw row with directory paths and file names
in one row. 
"""
import os

# set the master parent directory
path = input("Where is your top most parent directory? > ")

# print a row with directory paths and files inside
for file in os.walk(path):
    for filename in file:
        print(file)

