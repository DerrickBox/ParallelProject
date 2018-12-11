# -*- coding: utf-8 -*-
"""
* Ryan Jenkins
* Group 2
* Parallel Sort
"""
import multiprocessing as mp
import time
import random
from bubbleSort import bubbleSort


dataSize = 100
numProc = 1

bubbleSortID = 0


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
        print(aList[i])
     
        
"""
* main
"""
def main():
    #print("-> parallelSort.py -> main()")
    # Generate the list of numbers [1, dataSize] shuffled identically for each sorting algorithm
    dataList = generateLists(dataSize, numProc)
    printLists(dataList) # print for debugging generated lists of numbers
    
    # Sort lists using parallel processing
    # Setup pipe connection for communication between processes
    conn = [["",""] for i in range(numProc)]
    for i in range(numProc):
        conn[i][0], conn[i][1] = mp.Pipe()
        
    processes = []
    processes.append(mp.Process(target = bubbleSort, args = [conn[bubbleSortID][1], dataList[bubbleSortID],]))
    
    startTime = time.time()
    for p in processes: 
        p.start()
    
    response = [0 for i in range(numProc)]
    response[bubbleSortID] = conn[bubbleSortID][0].recv()
    
    for p in processes: 
        p.join()
    
    endTime = time.time()
    
    dataList[bubbleSortID] = response[bubbleSortID][0]
    
    printLists(dataList)
    elapsedTime = endTime - startTime
    print("Total Time Elapsed:", elapsedTime)


if __name__ == "__main__":
    main()