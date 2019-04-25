import time,random

"""
Function random creates random tests in file for binpack problem HW8
"""
import os,sys, random

def writeSameLine(inputText):
    with open('binRand300.txt', "a") as fileOut:
        fileOut.write(inputText)

def writeLine(inputText):
    with open('binRand300.txt', "a") as fileOut:
        fileOut.write(str(inputText))
        fileOut.write('\n')

def randomArray(size,low,high):
    i = 0
    while i < size:
        randNum = random.randint(low,high)
        writeSameLine((repr(randNum) + ' '),)
        i += 1
    with open('binRand300.txt', "a") as fileOut:
        fileOut.write('\n')

def main(n):
    try:
        if os.path.exists('binRand300.txt'):
            os.remove('binRand300.txt')
        tests = 4
        writeLine(tests)
        i = 0
        while i < tests:
            c = 300
            writeLine(c)
            writeLine(n)
            randomArray(n,1,c)
            i +=1

    except:
        print "fail"


if __name__ == "__main__":
   main(300)

