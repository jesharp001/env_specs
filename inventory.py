"""
The purpose of this script is to create an environment
inventory based on the output of scripts used for
sizing and capacity exercises.

Version 1: raw row with directory paths and file names with one file per row.

Python 3.7.1
"""
import os

# set the master parent directory
# uncomment the line below in final draft
# path = input("Where is your top most parent directory? > ")
#
# hard code test directory below for testing convenience
path = 'c:/pythontest'

"""

# print a row with directory paths and files inside
for file in os.walk(path):
    for filename in file:
        print(file)

# visual line to separate test 1 from test 2)
print('-----------------------------------------------------------\n')
"""

# print each file/doc on a row with full path
# result of this for loop is de-duplicated rows
for subdir, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.zip'):
            pass
        else:
            print(os.path.join(subdir, file))

print('<--------------------------------------------------->')

#for subdir, dirs, files in os.walk(path):
    #for file in files:

        #print(os.path.isdir(file)) #returns False because class = str
        #print(type(file))
