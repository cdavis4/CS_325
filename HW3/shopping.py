"""Author Carrie Davis
Program:shopping.py takes an input txt file as argument in command line
outputs a text file in same folder as shopping.txt called results.txt
that gives information about optimal shopping for input test cases.
"""
import os,sys

def writeLine(inputText):
    print inputText
    with open("results.txt", "a") as fileOut:
        fileOut.write(inputText)
        fileOut.write('\n')

def writeSameLine(inputText):
    print inputText
    with open("results.txt", "a") as fileOut:
        fileOut.write(inputText)


def readLine(inputLine):
    array = []
    size = inputLine.split()[0]
    for c in inputLine.split()[1:]:
        array.append(c)
    return size, array

"""line number and F is the line[lineNum] values of items array and their weight array to use in knapsack"""
def shoppingSpree(lineNum,member,F,val,wt):
    Total = 0
    f = 1
    print"Member Items"
    writeLine("Member Items")
    while F > 0:
        lineNum += 1
        W = int(member[lineNum]) # carrying weight for that family member
        price, items = knapSack(W,wt,val,len(wt))
        printSelectedItems(f,items, W, wt, val)
        Total += price
        F -=1
        f+=1
    writeLine("Total Price " + repr(Total))
    return lineNum

"""filling the value and weight arrays N is the line[lineNum] in input file"""
def fillArrays(lineNum,line,N):
    wt = []  # [30,10,40,10,5]
    val = []
    N = int(N)
    lineNum = int(lineNum)

    while N > 0:
        lineNum +=1
        p,w = line[lineNum].split() #values and weight for item
        val.append(int(p))
        wt.append(int(w))
        N -= 1
    return wt,val,lineNum


def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    Items = [[0 for x in range(W + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                if val[i - 1] + K[i - 1][w - wt[i - 1]] > K[i - 1][w]:
                    K[i][w] = val[i - 1] + K[i - 1][w - wt[i - 1]]
                    Items[i-1][w] = 1 # means item is in knapsack
                else:
                    K[i][w] = K[i - 1][w]
                    Items[i-1][w] = 0 # means item is not in knapsack
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W],Items

def printSelectedItems(f,Items, W, wts, val):
    #writing out what items picked
    writeSameLine(repr(f) + ': ',)
    K = W
    i = len(val) -1
    wsel = 0
    vsel = 0
    while i >= 0:  # need to go in the reverse order
        if Items[i][K] == 1:
            writeSameLine((repr(i+1) + ' '), )
            wsel += wts[i]
            vsel += val[i]
            K = K - wts[i]
        i-=1
    writeLine('')


def main(argv):
    try:
        if os.path.exists('results.txt'):
            os.remove('results.txt')
        if argv.endswith('.txt'):
            file = open(argv)
            lines = file.readlines() #read specific lines
            tests = int(lines[0])
            test = 1
            lineNum = 1
            while tests != 0:
                writeLine("Test Case " + repr(test))
                test +=1
                wt,val, lineNum = fillArrays(lineNum, lines, lines[lineNum])
                tests -=1
                lineNum = int(lineNum) +1
                F = int(lines[lineNum])
                lineNum = shoppingSpree(lineNum,lines, F, val, wt)
                lineNum +=1
            file.close()


    except:
        print "fail"


if __name__ == "__main__":
    if len(sys.argv) >1:
        input = sys.argv[1]
        main(input)
    else:
        main("shopping.txt")
