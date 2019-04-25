"""Author Carrie Davis
Program:shopping.py takes an input txt file as argument in command line
outputs a text file in same folder as shopping.txt called results.txt
that gives information about optimal shopping for input test cases.
"""
import os,sys
def writeLine(inputArray):
    print inputArray
    with open("shopping.txt", "a") as fileOut:
        fileOut.write(' '.join(map(str,inputArray)))
        fileOut.write('\n')

def readLine(inputLine):
    array = []
    size = inputLine.split()[0]
    for c in inputLine.split()[1:]:
        array.append(c)
    return size, array