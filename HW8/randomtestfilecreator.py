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

def randomArray(size,low,high,inFile,filewrite):
    i = 0
    while i < size:
        randNum = random.randint(low,high)
        filewrite.writeLine((repr(randNum) + ' '),)
        i += 1
    filewrite.writeLine('\n')
    
def main(n):
    try:
        file = 'binRand300.txt'
        if os.path.exists(file):
            os.remove(file)
        wfile = WriteToText(file)
        tests = 4
        wfile.writeLine(tests,'')
        i = 0
        while i < tests:
            c = 300
            wfile.writeLine(c)
            wfile.writeLine(n)
            randomArray(n,1,c,file,wfile)
            i +=1
    except Exception as e:
        print("fail: ",e)

if __name__ == "__main__":
   main(300)

