# HW3 Q2 Shopping Spree Code

This is the readme for running python code created for ANALYSIS OF ALGORITHMS (CS_325_400_W2019) HW3 question 2. This code implements the knapsack algorithm to solve a problem of what items in a family shopping spree to grab if each item is defined by integer weight and value and each family member has their own carrying capacity. Duplicates in types of items can be allowed within family but not for each individual. We must determine which types(items) the family members should grap to get the best value (highest price of merchandice) as a whole.

## Getting Started
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to run the project on engineering server.

### Prerequisites
Text file must be in same folder as python script shopping.py and the text must be organized as below.
- text file formated with first line as # number of test cases (1-100). Then for each test case:
- next line is int number N that indicates the number of items (1-100).
- next N line(s) represent the items price P(1 - 500) and weight W(1-100) corresponding to the weight of object
- next line contains one integer F (1-30) representing number of people in family.
- next F line(s) represent a family member's carry capacity in pds (1-200).

Sample Input
```
2 
3
72 17 
44 23 
31 24 
1
26
2
64 26 
85 22 
1
23 
20
```

## Deployment
----

1) Run program of choice in cmd line and define the input text file. example:  `python shopping.py 'shopping.txt'`

2) Output results will be printed to commandline terminal as defined in HW2 instructions

## Built With
---
* [python](https://docs.python.org/) - python 2.7.5
* imported os, sys to use arv come with python as default

## Author
---
* **Carrie Davis** 

## Resources
---
* knapsack algorithm: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
* printing knapsack: https://sadakurapati.wordpress.com/2013/11/30/algorithm-knapsack/

