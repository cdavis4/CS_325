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


def mergeSort(sortedArray):
    if 1 < len(sortedArray):
        q = len(sortedArray)//2
        left = sortedArray[:q]
        right = sortedArray[q:]
        mergeSort(left)
        mergeSort(right)
        merge(left,right,sortedArray)

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



def main():
    try:
        line = 1
        for i in n:
            array = randomArray(i,0,10000)
            start = time.time()
            mergeSort(array)
            end = time.time()
            print"#", line, ("Array Size: ", i, "Running Time (sec) ", end - start)
            line +=1

    except:
        print "fail"

if __name__ == "__main__":

    main()