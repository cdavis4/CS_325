"""
This program takes input data from txt file that represents activity sets
defined on first line as n. Then for n lines representing individual activities
id,start time, finish time. So on depending on how many activity sets are listed.
The program sorts activities into a list from latest start to earliest start time.
Then uses a greedy approach to find which ones will fit into a schedule without conflict
Information about # of sets of activities, # of activities.
example of input activity set when formatted into dict:
A = [ { 'id' :  3, 's' : 6, 'f' :  8} ,
                        { 'id' :  1, 's' : 7, 'f' : 9} ,
                        { 'id' : 2, 's' : 1, 'f' :  2} 
                       ]
"""


import sys

def mergeSort(sortedArray,sortVal = ''):
    if 1 < len(sortedArray):
        q = len(sortedArray)//2
        left = sortedArray[:q]
        right = sortedArray[q:]
        mergeSort(left,sortVal)
        mergeSort(right,sortVal)
        merge(left,right,sortedArray,sortVal)

def merge(L,R, finalArray,sortVal=''):
    i = 0 # left half index
    j = 0 # right half index
    index = 0 #for merged array
    if sortVal != '' and type(finalArray[0] == 'dict'):
        while i < len(L) and j < len(R):
            if L[i].get(sortVal) >= R[j].get(sortVal):
                finalArray[index] = L[i]
                i += 1
            else:
                finalArray[index] = R[j]
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

    else:
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

def greedy_activity_selector(array):
    try:
        n = len(array)
        S =[]
        S.append(array[0])
        k = 0
        for a in range(1, n):
            if array[a].get('f') <= S[k].get('s'):
                S.append(array[a])
                k +=1
        return S

    except:
        print "fail"

def printSchedule(array):
    #printing schedule in order of starting time
    print("Number of activities selected ="),
    n = len(array)
    print (repr(n))
    i = n -1
    print("Activities: "),
    while i >= 0:  # need to go in the reverse order
        print(repr(array[i].get('id')) + ' '),
        i-=1
    print '\n'


def readLine(inputLine):
    array = []
    size = inputLine.split()[0]
    for c in inputLine.split()[1:]:
        array.append(c)
    return size, array

"""create dict for activity using line[lineNum] in input file"""
def createAct(line,lineNum):
    lineNum = int(lineNum)
    id,s,f = line[lineNum].split(' ')
    act = {}
    act['id'] = int(id)
    act['s'] = int(s)
    act['f'] = int(f)
    return act

def activitySet(line,lineNum):
    sets = line[lineNum]
    A = []
    setVal = int(sets)
    lineNum +=1
    while setVal > 0:
        act = createAct(line,lineNum)
        A.append(act)
        setVal -= 1
        lineNum += 1
    mergeSort(A, 's')
    Schedule = greedy_activity_selector(A)
    printSchedule(Schedule)
    return lineNum  #next line

def main(argv):
    try:
        if argv.endswith('.txt'):
            file = open(argv)
            lines = file.readlines()
            endOfLine = len(lines)
            lineNum = 0
            #read specific lines
            i = 0 # set counter
            while lineNum < endOfLine:
                i += 1
                print '\n' + "Set " + repr(i)
                lineNum = activitySet(lines, lineNum)

            file.close()

    except:
        print "fail"

if __name__ == "__main__":
    if len(sys.argv) >1:
        input = sys.argv[1]
        main(input)
    else:
        main("act.txt")

