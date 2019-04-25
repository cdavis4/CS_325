# HW8 Q1 Aproximation Bin Packing Code

This is the readme for running python code created for ANALYSIS OF ALGORITHMS (CS_325_400_W2019) HW8 question 1. This code implements bin packing aproximation algorithms to solve a problem of what items will fit in bins and how to select the least number of bins. Each item is defined by integer weight and each bin has a shared carrying capacity. 

## Getting Started
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to run the project on engineering server.

### Prerequisites
Text file must be in same folder as python script binpack.py and the text must be organized as below.
- text file formated with first line as # number of test cases (1-100). Then for each test case:
- next line contains one integer C (k -100) with k representing a # that can not be less than the largest item.
- next line is int number N that indicates the number of items (1-100).
- next N line(s) represent the items weight (1 - 500) corresponding to the weight of object
`
Sample Input
3
10
6
5 10 2 5 4 4
20
19
9 10 2 1 7 3 3 3 3 14 6 5 2 8 6 4 6 2 6
10
20
4 4 4 4 4 4 4 4 4 4 6 6 6 6 6 6 6 6 6 6
`
## Deployment
----
1) To run on flip (OSU engineering server) unzip folder on server to directory of choice.  Program(s) require at least python 2.7 which is installed on flip. Using Command line, navigate to folder containing scripts example:
`flip3 ~ 154% cd Algorithms/HW8`

2) Run program of choice in cmd line and define the input text file. By default if no text entered will use 'bin.txt'. example:  `python binpack.py 'bin.txt'` or just `python binpack.py`

4) Output results will be printed to commandline terminal as defined in HW8 instructions

## Built With
---
* [python](https://docs.python.org/) - python 2.7.5
* imported sys to use arv come with python as default

## Author
---
* **Carrie Davis** - *OSU Student ID#933615388*

## Resources
---
* bin-packing algorithm: Basic Analysis of Bin-Packing Heuristics, Rieck, B.: http://bastian.rieck.ru/research/Note_BP.pdf



