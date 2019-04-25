import time,random

"""
Function random creates random values in array
input # of values desired, low range value and highest in range value
outputs array
"""

n = [100, 250, 500, 1000, 2500, 3000, 5000, 10000, 15000, 20000]

def randomArray(size,low,high):
    randArray = []
    i = 0
    while i < size:
        randNum = random.randint(low,high)
        randArray.append(randNum)
        i += 1
    return randArray


def mergeSort(sortedArray,first,last):
    if first < last:

       # print("Splitting ", sortedArray)

        mid1 = int((first + (last))/2)
        mid2 = int((first + mid1) / 2)
        mid3 = int((mid1+1)+last)/2
        mergeSort(sortedArray, first, mid2)
        mergeSort(sortedArray, mid2+1, mid1)
        mergeSort(sortedArray, mid1+1, mid3)
        mergeSort(sortedArray, mid3+1, last)
        merge(sortedArray, first,last, mid1, mid2, mid3)

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
   # print("Merged ", finalArray)


def main():
    try:
        line = 1
        for i in n:
            array = randomArray(i,0,10000)
            start = time.time()
            mergeSort(array, 0, len(array) - 1)
            end = time.time()
            print"#", line, ("Array Size: ", i, "Running Time (sec) ", end - start)
            line +=1

    except:
        print "fail"

if __name__ == "__main__":

    main()