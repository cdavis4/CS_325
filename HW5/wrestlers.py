"""
This program takes input data from txt file that represents wrestlers defined on first line as n.
Then for n lines values represent individual wrestlers. The next line represents r the number of rivalries.
Then for r lines the values represent 2 wrestlers that are rivals using a space to delineate between names.
The program will assign the first wrestler a "babyface" and use the rivalry data to determine which wrestlers are
babyfaces and which are heels.  Requirement to be rivals the wrestlers can not be both babyfaces or both heels.
The program will determine if input data breaks this requirement. If so it will print out "No, Not Possible". If possible
the program will print out Yes. Next line will be Babyfaces: list of wrestler's of this type. Next line Heels: list of
wrestlers of this type.

This program uses breadth-first search and create a graph to find which wrestlers are Babyfaces and/or Heels. Wrestlers
are V and rivalries are E.
"""
import sys

def addWrestler(inputLine, inputGraph):
    inputGraph[inputLine.rstrip()] = {}

"""create dict for wrestler"""
def createWrestler(inputLine, inputGraph,inputType=None):
    wrestler = {}
    wrestler['name'] =inputLine.rstrip()
    wrestler['rivals'] = []
    wrestler['type'] = inputType
    return wrestler

"""returns index value in list for dict
enumerate is O(n) as it's an iterator"""
def find(key, value, inputGraph):
    identifier = next(i for i, item in enumerate(inputGraph) if item[key] == value)
    return identifier

def addRival(rivals,inputGraph):
    key,value = rivals.split(' ')
    rival= value.rstrip()
    index = find("name",key,inputGraph)
    inputGraph[index]['rivals'].append(rival)
    index = find("name",rival,inputGraph)
    inputGraph[index]['rivals'].append(key)


def identifyWrestlerType(inputGraph):
    index = find("type", 'babyfaces', inputGraph)
    bfs(inputGraph,inputGraph[index].get("name"))
    for a in range(1, len(inputGraph)):
        if inputGraph[a].get('rivals') != [] and inputGraph[a].get('type') == None:
            start = inputGraph[a].get('name')
            #This is a disconnected new graph must assign first type
            inputGraph[a]['type'] ='babyfaces'
            bfs(inputGraph,start)

def bfs(graph, start):
    queue = [start]
    explored = []
    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            index = find("name", node, graph)
            pType = graph[index].get('type')
            neighbors = graph[index].get('rivals')
            for neighbor in neighbors:
                index = find('name', neighbor, graph)
                if graph[index].get('type') == pType:
                    print "Impossible"
                    exit(0)
                else:
                    if pType == 'babyfaces':
                        graph[index]['type'] = 'heels'
                    else: graph[index]['type'] = 'babyfaces'
                queue.append(neighbor)


def printWrestlers(inputType, inputGraph):
    print(inputType.capitalize() + ": "),
    for w in inputGraph:
        if w.get('type') == inputType:
            print w.get("name"),
    print '\n'

def main(argv):
    if argv.endswith('.txt'):
        file = open(argv)
        lines = file.readlines()
        n = int(lines[0])
        if n > 0:
            #create representation of graph with wrestlers
            graph = []
            lineNum = 1
            while lineNum <= n:
                if lineNum == 1:
                    wrestler = createWrestler(lines[lineNum],graph,'babyfaces')
                else:
                    wrestler = createWrestler(lines[lineNum],graph)
                graph.append(wrestler)
                lineNum +=1
            r = int(lines[lineNum])
            if r > 0:
                while r > 0:
                    lineNum +=1
                    addRival(lines[lineNum], graph)
                    r -=1
            #run bfs on wrestlers to identify type from rivals
            identifyWrestlerType(graph)
            #print output to terminal
            print "Yes Possible"
            printWrestlers('babyfaces', graph)
            printWrestlers('heels', graph)
        else: print("Did not specify number of wrestlers in file")
        file.close()

if __name__ == "__main__":
    if len(sys.argv) >1:
        input = sys.argv[1]
        main(input)
    else:
        main("wrestler.txt")


