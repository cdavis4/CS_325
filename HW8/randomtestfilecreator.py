import time,random

"""
Function random creates random tests in file for binpack problem HW8
"""
import os,sys, random

class WriteToText():
    def __init__(self,inputFile):
        self.text = ""
        self.file = inputFile
    def writeLine(self,inputText="", inChar=''):
        self.text = str(inputText)
        with open(self.file, "a") as fileOut:
            fileOut.write(self.text)
            if inChar == '\n' or inChar == '\t':
                fileOut.write(inChar)

def randomArray(size,low,high,filewrite):
    i = 0
    while i < size:
        randNum = random.randint(low,high)
        if i < (size-1):
            filewrite.writeLine(str(randNum) + ' ,')
        else:
            filewrite.writeLine(str(randNum))
        i += 1
    filewrite.writeLine('\n')

def main(n):
    try:
        file = 'binRand300.txt'
        if os.path.exists(file):
            os.remove(file)
        wfile = WriteToText(file)
        tests = 4
        wfile.writeLine(tests,'\n')
        i = 0
        while i < tests:
            c = 300
            wfile.writeLine(c,'\n')
            wfile.writeLine(n,'\n')
            randomArray(n,1,c,wfile)
            i +=1
    except Exception as e:
        print("fail: ",e)

if __name__ == "__main__":
   main(300)

