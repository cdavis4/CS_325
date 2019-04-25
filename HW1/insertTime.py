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
      #  print i
        randNum = random.randint(low,high)
        randArray.append(randNum)
        i += 1
    return randArray


def insertSort(sortedArray):
    for index in range(1,len(sortedArray)):
        j = index
        val = sortedArray[index]
        while j > 0 and sortedArray[j-1] > val:
            sortedArray[j] = sortedArray[j-1]
            j -= 1
        sortedArray[j] = val
    return sortedArray




def main():
    try:
        line = 1
        for i in n:
            array = randomArray(i,0,10000)
            start = time.time()
            sortedA = insertSort(array)
            end = time.time()
            print"#", line, ("Array Size: ", i, "Running Time (sec) ", end - start)
            line +=1

    except:
        print "fail"

if __name__ == "__main__":

    main()