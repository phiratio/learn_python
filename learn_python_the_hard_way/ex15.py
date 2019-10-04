# import argv library so we can use it
from sys import argv

# assign variables to arguments, first argument is always the script itself
script, filename = argv
# assign variable txt to output of a function open which takes filename from argv
txt = open(filename)
# prints a msg
print("Here's your file %r:" % filename)
# prints the content of a file  :TODO why it's a 2 step process -> open(filename) and then read
print(txt.read())
txt.close()
# get input one more time
print("Type the filename again:")
file_again = input("> ")

# read from that input nad print content of file if exists
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
