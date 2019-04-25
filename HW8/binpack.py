"""Author Carrie A Davis
Program: binpack.py Input text:first line is the number of test cases,
followed by the capacity of bins for that test case,
the number of items and then the weight of each item.
 The program will use 3 different binpacking algorithms to solve and find
 minimum number of bins for storage. Output terminal:
 Test case # name of algorithm: bins, .. for each test cas
 """

import sys


def mergeSort(sortedArray):
    #print("Splitting ", sortedArray)
    if 1 < len(sortedArray):
        q = len(sortedArray)//2
        left = sortedArray[:q]
        right = sortedArray[q:]
        mergeSort(left)
        mergeSort(right)
        merge(left,right,sortedArray)
    #print("Merged ", sortedArray)

def merge(L,R, finalArray):
    i = 0 # left half index
    j = 0 # right half index
    index = 0 #for merged array
    while i < len(L) and j < len(R):
        if L[i] >= R[j]:
            finalArray[index]=L[i]
            i += 1
        else:
            finalArray[index]=R[j]
            j += 1
        index += 1
    while i < len(L):
        finalArray[index] = L[i]
        i += 1
        index += 1
    while j < len(R):
        finalArray[index] = R[j]
        j += 1
        index += 1

def firstFit(items,c):
    if c > 0 and len(items) > 0:
        bins = []
        bins.append(c)
        for item in items:
            n = len(bins)
            j=0
            while j < n:
                if item <= bins[j]:
                    bins[j] -= item
                    break
                if j == (n-1):
                    weight = c-item
                    bins.append(weight)
                j += 1
    return len(bins)

def bestFit(items,c):
 #max item must be <= c
    if len(items) > 0 and c > 0:
        bins = []
        weight = c-items[0]
        bins.append(weight)
        for item in items[1:]:
            j = 0
            i = 0
            min = c + 1
            for bin in bins:
                j += 1
                if(bin >= item) and (bin - item < min):
                    min = bin-item
                    i=j-1
            if min == c + 1:
                weight = c - item
                bins.append(weight)
            else:
                bins[i] = min
            mergeSort(bins)
    return len(bins)


def main(argv):
    try:
        if argv.endswith('.txt'):
            file = open(argv)
            lines = file.readlines()
            tests = int(lines[0])
            test = 1 #counter
            lineNum = 1 #startlinecount
            while tests > 0:
                C = int(lines[lineNum])
                lineNum += 1
                itemNum = lines[lineNum]
                lineNum += 1
                items = lines[lineNum].split()
                lineNum += 1
                itemArray = []
                for item in items:
                    itemArray.append(int(item))
                #First Fit bins
                bins1 = firstFit(itemArray, C)
                # Best Fit Bins
                bins3 = bestFit(itemArray, C)
                mergeSort(itemArray)
                # First Fit Decreasing bins
                bins2 = firstFit(itemArray, C)
                print "Test Case " + repr(test) + " First Fit: " + \
                      repr(bins1) + ", First Fit Decreasing: " + \
                      repr(bins2) + ", Best Fit: " + repr(bins3)
                tests -=1
                test +=1

    except:
        print "fail"

if __name__ == "__main__":
    if len(sys.argv) >1:
        input = sys.argv[1]
        main(input)
    else:
        main('bin.txt')