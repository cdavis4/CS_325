# HW4 Q4 Last to Start Activity Scheduler Code

This is the readme for running python code created for ANALYSIS OF ALGORITHMS (CS_325_400_W2019) HW4 question 4. This code implements the greedy activity algorithm to solve a problem to maximize the number of activities can be scheduled that do not conflict time wise with each other. Activites are sorted from last to start. Schedule is created with activies where time frame of one activity does not overlap with another.

## Getting Started
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to run the project on engineering server.

### Prerequisites
Text file must be in same folder as python script last_to_start.py and the text must be organized as below.
- text file formated with first line as # number of activities in a set. Then for each set:
- next line has 3 numbers separated by space that represent the activity id, start time and finish time as integers.

Sample Input
```
11
1 1 4
2 3 5
3 0 6
4 5 7
5 3 9
6 5 9
7 6 10
8 8 11
9 8 12
10 2 14
11 12 16
3
3 6 8
1 7 9
2 1 2
```
## Deployment
----

1) Run program in cmd line and define the input text file or use default which is set to use 'act.txt' file. 
example:  `python activity.py 'act.txt'` or
example:  `python activity.py ` to use default 'act.txt' file

2) Output results will be printed to commandline terminal as defined in HW4 instructions

## Built With
---
* [python](https://docs.python.org/) - python 2.7.5
* imported sys to use arv come with python as default

## Author
---
* **Carrie Davis** 

## Resources
---
* greedy algorithm: CLRS Intro to Algorithms 16.1



