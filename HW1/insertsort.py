"""Author Carrie Davis
Program:insertsort.py takes an input txt file as argument in command line
outputs a text file in same folder as insert.txt with array sorted using
insertion sort algorithm
"""
import os,sys
def writeLine(inputArray):
    print inputArray
    with open("insert.txt", "a") as fileOut:
        fileOut.write(' '.join(map(str,inputArray)))
        fileOut.write('\n')


def readLine(inputLine):
    array = []
    size = inputLine.split()[0]
    for c in inputLine.split()[1:]:
        array.append(c)                                                       
    return size, array

def insertSort(sortedArray,size):
    print ('Unsorted Array')
    print sortedArray
    sortedArray = list(map(int, sortedArray))
    for index in range(1,len(sortedArray)):
        j = index
        val = sortedArray[index]
        while j > 0 and sortedArray[j-1] > val:
            sortedArray[j] = sortedArray[j-1]
            j -= 1
        sortedArray[j] = val
    print ("Array sorted ")
    return sortedArray

def main(argv):
    try:
        if os.path.exists('insert.txt'):
            os.remove('insert.txt')
        if argv.endswith('.txt'):
            with open(argv) as file:
                for line in file:
                    outSize, outArray = readLine(line)
                    array = insertSort(outArray,outSize)
                    writeLine(array)
    except:
        print "fail"

if __name__ == "__main__":
    if len(sys.argv) >1:
        input = sys.argv[1]
        main(input)
    else:
        main("data.txt")