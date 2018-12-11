# -*- coding: utf-8 -*-
"""
* Ryan Jenkins
* Group 2
* Parallel Sort
"""
import sys
import multiprocessing as mp
import time
import random
from bubbleSort import multiBubbleSort
from insertionSort import multiInsertionSort
from quickSort import multiQuickSort


PARENT = 0
CHILD = 1


sort = [multiBubbleSort, multiInsertionSort, multiQuickSort]
sortName = ["Bubble Sort", "Insertion Sort", "Quick Sort"]



"""
* Return a list of integers from 1 to the data size
"""
def generateLists(size, quantity):
    #print("-> parallelSort.py -> generateLists()")
    aList = [i for i in range(size)]
    random.shuffle(aList)
    aList = duplicateList(aList, quantity)
    return aList


"""
* Return a list of a specified number of lists with values copied from a provided list
"""
def duplicateList(aList, size):
    #print("-> parallelSort.py -> duplicateList()")
    dupList = [[] for i in range(size)]
    for i in range(size):
        dupList[i] = [aList[j] for j in range(len(aList))]   
    return dupList


"""
* Print the values of provided lists
"""
def printLists(aList):
    #print("-> parallelSort.py -> printLists()")
    for i in range(len(aList)):
        print(sortName[i])
        print(aList[i])
     
        
"""
* main
"""
def main(argv):
    #print("-> parallelSort.py -> main()")
    # Set the data size from the command line
    dataSize = 100
    if len(argv) > 1:
        dataSize = int(argv[1])

    # Generate the list of numbers [1, dataSize] shuffled identically for each sorting algorithm
    dataList = generateLists(dataSize, len(sort))
    #printLists(dataList) # print for debugging generated lists of numbers
    
    # Sort lists using parallel processing
    startTime = time.time()
    # Setup pipe connection for communication between processes
    conn = [["",""] for i in range(len(sort))]
    for i in range(len(sort)):
        conn[i][PARENT], conn[i][CHILD] = mp.Pipe()
    
    # Initialize processes for sorting algorithms
    processes = []
    for i in range(len(sort)):
        processes.append(mp.Process(target = sort[i], args = [conn[i][CHILD], dataList[i],]))
    for p in processes: 
        p.start()
    
    # Recieve results from processes through Pipe
    response = [0 for i in range(len(sort))]
    for i in range(len(sort)):
        response[i] = conn[i][PARENT].recv()
    
    # Join processes at end of multiprocessing section
    for p in processes: 
        p.join()
    endTime = time.time()

    # load sorted lists and completions times from responses and output results
    elapsedTime = [0 for i in range(len(sort))]
    for i in range(len(sort)):
        dataList[i] = response[i][0]
        elapsedTime[i] = response[i][1]
    print()
    for i in range(len(dataList)):
        print(sortName[i], "Elapsed Time:", elapsedTime[i])
        #print(dataList[i])
    print("\nTotal Time Elapsed:", endTime - startTime)


if __name__ == "__main__":
    main(sys.argv[0:])
