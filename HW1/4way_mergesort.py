"""Author Carrie A Davis
Program: mergesort.py input text file containing arrays of integers
 separating each array by a new line and numbers with space with
 first value in each line being the size of the array
 example text line would contain 6 1 2 2 3 3 2
 The program will sort each array one line at a time
 writing sorted array outputs to a file called merge.txt
 credits for algorithm development http://interactivepython.org/runestone/static/pythonds/index.html"""

import os,sys

def writeLine(inputArray):
    print inputArray
    with open("merge.txt", "a") as fileOut:
        fileOut.write(' '.join(map(str,inputArray)))
        fileOut.write('\n')


def readLine(inputLine):
    array = []
    size = inputLine.split()[0]
    for c in inputLine.split()[1:]:
        array.append(c)
    return size, array


def mergeSort(sortedArray):
    print("Splitting ", sortedArray)
    if 1 < len(sortedArray):
        q = len(sortedArray)//2
        left = sortedArray[:q]
        right = sortedArray[q:]
        mergeSort(left)
        mergeSort(right)
        merge(left,right,sortedArray)
    print("Merged ", sortedArray)

def merge(L,R, finalArray):
    i = 0 # left half index
    j = 0 # right half index
    index = 0 #for merged array
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
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


def main(argv):
    try:
        if os.path.exists('merge.txt'):
            os.remove('merge.txt')
        if argv.endswith('.txt'):
            with open(argv) as file:
                for line in file:
                    outSize, outArray = readLine(line)
                    print ('Unsorted Array')
                    print outArray
                    mergeArray = list(map(int, outArray))
                    mergeSort(mergeArray)
                    writeLine(mergeArray)
    except:
        print "fail"

if __name__ == "__main__":
    if len(sys.argv) >1:
        input = sys.argv[1]
        main(input)
    else:
        main("data.txt")