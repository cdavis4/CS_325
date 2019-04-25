# HW2 4 way merge sort code 

This is the readme for running python code created for ANALYSIS OF ALGORITHMS (CS_325_400_W2019) HW2 question 5

## Getting Started
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to run the project on engineering server.

### Prerequisites

- Input Text file ('data.txt') The text file containing information to create arrays to run the program, example is included in zip.
first integer in line represents size of array (aka # of integers listed in text line) 

For example in 'data.txt'
```
10 10 9 8 7 6 5 4 3 2 1
3 8 8 8
8 1 3 4 1 4 7 3 5
```
Results (ouput) in txt file
```
1 2 3 4 5 6 7 8 9 10
8 8 8
1 1 3 3 4 4 5 7
```
## Deployment
----

1) Create and place text file containing arrays to be sorted in same folder as scripts

2) Run program of choice in cmd line. example:  `python 4way_mergesort.py "data.txt" `
If no filename is given on the command line, the program will try to read default file name in folder called 'data.txt'

3) Output results will be saved in same folder as either 'merge4.txt'.   

## Built With
---
* [python](https://docs.python.org/) - python 2.7.5
* imported basic lib os,sys come with python as default

## Acknowledgments
---
* readme template: https://gist.github.com/PurpleBooth/109311bb0361f32d87a2

# HW1 Q5 4Way MergeSort Running Time Eval code 

This is the readme for running python code created for ANALYSIS OF ALGORITHMS (CS_325_400_W2019) HW2 question 5

## Getting Started
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to run the project on engineering server.

### Prerequisites
- none

## Deployment
----
1) To run on flip (OSU engineering server) unzip folder on server to directory of choice.  Program(s) require at least python 2.7 which is installed on flip. Using Command line, navigate to folder containing scripts example:
`flip3 ~ 154% cd Algorithms/HW2/HW2code/`

2) Run program of choice in cmd line. example:  `python merge4Time.py`

4) Output results will be printed to commandline terminal as defined in HW2 instructions

## Built With
---
* [python](https://docs.python.org/) - python 2.7.5
* imported basic lib time,random come with python as default

## Author
---
* **Carrie Davis**

## Acknowledgments
---
* readme template: https://gist.github.com/PurpleBooth/109311bb0361f32d87a2





