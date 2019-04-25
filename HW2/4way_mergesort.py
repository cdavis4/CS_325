"""Author Carrie A Davis
Program: 4way_mergesort.py input text file containing arrays of integers
 separating each array by a new line and numbers with space with
 first value in each line being the size of the array
 example text line would contain 6 1 2 2 3 3 2
 The program will sort each array one line at a time
 writing sorted array outputs to a file called merge4.txt
 credits for algorithm development http://interactivepython.org/runestone/static/pythonds/index.html"""

import os,sys

def writeLine(inputArray):
    print inputArray
    with open("merge4.txt", "a") as fileOut:
        fileOut.write(' '.join(map(str,inputArray)))
        fileOut.write('\n')


def readLine(inputLine):
    array = []
    size = inputLine.split()[0]
    for c in inputLine.split()[1:]:
        array.append(c)
    return size, array

def merge(finalArray,low,high,mid1,mid2,mid3):
    first = mid2 - low + 1
    second = mid1- mid2
    third = mid3-mid1
    forth = high-mid3
    L = mid1-low+1
    R = high-mid1

    a = [0] * (first)
    b = [0] * (second)
    c = [0] * (third)
    d = [0] * (forth)
    left = [0] * (L)
    right = [0] * (R)

    for i in range(0, first):
        a[i] = finalArray[low + i]
    for i in range(0, second):
        b[i] = finalArray[mid2+1 + i]
    for i in range(0, third):
        c[i] = finalArray[mid1+1 + i]
    for i in range(0, forth):
        d[i] = finalArray[mid3+1 + i]
    i=0
    j=0
    index=0
    while i < first and j < second:
        if a[i] <= b[j]:
            left[index] = a[i]
            i += 1
        else:
            left[index] = b[j]
            j += 1
        index += 1
    while i < first:
        left[index] = a[i]
        i += 1
        index += 1

    while j < second:
        left[index] = b[j]
        j += 1
        index += 1
    i=0
    j=0
    index=0
    while i < third and j < forth:
        if c[i] <= d[j]:
            right[index] = c[i]
            i += 1
        else:
            right[index] = d[j]
            j += 1
        index += 1
    while i < third:
        right[index] = c[i]
        i += 1
        index += 1

    while j < forth:
        right[index] = d[j]
        j += 1
        index += 1
    i=0
    j=0
    index=low
    while i < L and j < R:
        if left[i] <= right[j]:
            finalArray[index] = left[i]
            i += 1
        else:
            finalArray[index] = right[j]
            j += 1
        index += 1
    while i < L:
        finalArray[index] = left[i]
        i += 1
        index += 1

    while j < R:
        finalArray[index] = right[j]
        j += 1
        index += 1
    print("Merged ", finalArray)

def mergeSort(sortedArray,first,last):
    if first < last:

        print("Splitting ", sortedArray)

        mid1 = int((first + (last))/2)
        mid2 = int((first + mid1) / 2)
        mid3 = int((mid1+1)+last)/2
        mergeSort(sortedArray, first, mid2)
        mergeSort(sortedArray, mid2+1, mid1)
        mergeSort(sortedArray, mid1+1, mid3)
        mergeSort(sortedArray, mid3+1, last)
        merge(sortedArray, first,last, mid1, mid2, mid3)


def main(argv):
    try:
        if os.path.exists('merge4.txt'):
            os.remove('merge4.txt')
        if argv.endswith('.txt'):
            with open(argv) as file:
                for line in file:
                    outSize, outArray = readLine(line)
                    print ('Unsorted Array')
                    print outArray
                    mergeArray = list(map(int, outArray))
                    mergeSort(mergeArray, 0,len(mergeArray)-1)
                    writeLine(mergeArray)
    except:
        print "fail"

if __name__ == "__main__":
    if len(sys.argv) >1:
        input = sys.argv[1]
        main(input)
    else:
        main("data.txt")