'''
Below program can be be done either using split() and join() methods OR using replace() method in python
'''


# import libraries
import sys


# take input from console
text = sys.stdin.read()

# split into lines by period
text = text.split(". ")

# newline after each line
text = '.\n'.join(text)

# display the sentences
print(text)

