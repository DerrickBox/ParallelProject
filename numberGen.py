"""
* Ryan Jenkins
* CSC 338 Group Project: Group 2
* numberGen.py
"""
import random, sys


"""
* Generate quantity lists with size elements from [1, size] or [lower, upper] 
* randomly, then shuffle the lists identically or separately.
"""
def generateLists(size, quantity, shuffleSync, listType, lower, upper):
    #print("-> parallelSort.py -> generateLists()")
    aList = [0 for i in range(size)]
    # Generate an ordered list [1, size], or of random ints [lower, upper]
    if (listType == 0):
        aList = orderedList(size)
    elif (listType == 1):
        aList = randomList(lower, upper, size)
    # Shuffle lists identically or differently
    if shuffleSync:
        aList = shuffleList(aList)
        aList = duplicateList(aList, quantity)
    else:
        aList = duplicateList(aList, quantity)
        for i in range(quantity):
            aList[i] = shuffleList(aList[i])
    return aList


"""
* Return a list of a specified number of lists with values copied from a provided list
"""
def duplicateList(aList, quantity):
    #print("-> parallelSort.py -> duplicateList()")
    dupList = [[] for i in range(quantity)]
    for i in range(quantity):
        dupList[i] = [aList[j] for j in range(len(aList))]   
    return dupList


"""
* Generate a list from 1 to size
"""
def orderedList(size):
    aList = [i+1 for i in range(size)] 
    return aList


"""
* Generate a list of random integers from a through b
"""
def randomList(lower, upper, size):
    if(lower > upper):
        temp = lower
        lower = upper
        upper = temp
    aList = []
    for i in range(size):
        aList.append(random.randint(lower, upper))
    return aList


"""
* Shuffle the items in provided list
"""
def shuffleList(aList):
    for i in range(random.randint(2, 3)):
        random.shuffle(aList)
    return aList


"""
* Main
"""
def main(argv):
    aList = orderedList(10)
    print(aList)
    aList = shuffleList(aList)
    print(aList)
    bList = generateLists(25, 2, True, 0, 0, 0) # Generate 2 lists [1, size] shuffled identically
    print(bList)
    cList = generateLists(10, 3, False, 1, -100, 100) # Generate 3 lists [-100, 100] shuffled differently
    print(cList)



if __name__ == "__main__":
    main(sys.argv)
    