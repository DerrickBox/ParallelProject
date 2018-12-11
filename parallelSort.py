# -*- coding: utf-8 -*-
"""
* Ryan Jenkins
* Group 2
* Parallel Sort
"""
import multiprocessing as mp
import time
import random
from bubbleSort import multiBubbleSort
from insertionSort import multiInsertionSort


PARENT = 0
CHILD = 1


dataSize = 100
sort = [multiBubbleSort, multiInsertionSort]
sortName = ["Bubble Sort", "Insertion Sort"]



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
def main():
    #print("-> parallelSort.py -> main()")
    # Generate the list of numbers [1, dataSize] shuffled identically for each sorting algorithm
    dataList = generateLists(dataSize, len(sort))
    printLists(dataList) # print for debugging generated lists of numbers
    
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

    # load sorted lists and completions times from responses
    for i in range(len(sort)):
        dataList[i] = response[i][0]
    
    printLists(dataList)
    elapsedTime = endTime - startTime
    print("Total Time Elapsed:", elapsedTime)


if __name__ == "__main__":
    main()
