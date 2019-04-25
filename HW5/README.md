# HW5 Q3 Wrestlers Code

This is the readme for running python code created for ANALYSIS OF ALGORITHMS (CS_325_400_W2019) HW5 question 3. This code implements the greedy activity algorithm breadth-first search to solve a problem to idenitify types of wrestlers as 'babyfaces' or 'heels'. Wrestlers are the vertices and edges that are rivalries between wrestlers. Based on input information on rivalries and that the first wrestler in a graph is 'babyface'. The idea is to use BFS to identify types of the rest of the wrestlers knowing only that wrestlers can not have the same type as their rival or in terms of the graph vertices should not be connected or adjacent to vertices that are the same type. This program determines the 'Heels' and the 'BabyFaces' using this information. Also, if information does not follow the rules in wrestler type the program will stop and print out "impossible". Prints list of 'BabyFaces' and list of 'Heels' if possible.

## Getting Started
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to run the project on engineering server.

### Prerequisites
Text file must be in same folder as python script wrestlers.py and the text must be organized as below.
- text file formated with first line as # number of wrestlers n. Then for the next n # of lines:
- wrestler name
- next line lists # number of rivalries r. Then for the next r # of lines:
- next line has 2 names separated by space that represent wrestlers with rivalry or edges in graph.

Sample Input
6
Bear
Maxxx
Killer
Knight
Duke
Samson
5
Bear Samson
Killer Bear
Samson Duke
Killer Duke
Maxxx Knight

// Sample Solution
Yes Possible
Babyfaces: Bear Maxx Duke
Heels: Killer Knight Samson

## Deployment
----
1) To run on flip (OSU engineering server) unzip folder on server to directory of choice.  Program(s) require at least python 2.7 which is installed on flip. Using Command line, navigate to folder containing scripts example:
`flip3 ~ 154% cd Algorithms/HW5/HW5_Davis_Carrie/`

2) Run program in cmd line and define the input text file or use default which is set to use 'act.txt' file. 
example:  `python wrestlers.py 'wrestler.txt'` or
example:  `python wrestlers.py ` to use default 'wrestler.txt' file

3) Output results will be printed to commandline terminal as defined in HW5 instructions

## Built With
---
* [python](https://docs.python.org/) - python 2.7.5
* imported sys to use arv come with python as default

## Author
---
* **Carrie Davis** - *OSU Student

## Resources
---
*bfs: Adapted from Python in Wonderland: 'https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/'



