
# Serial Selection Sort 
#modified from: http://interactivepython.org/
import time
import multiprocessing as mp


def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location
               #print(positionOfMax)
               #print(alist[positionOfMax])
       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp



def multiSelectionSort(conn, aList):
    startTime = time.time()
    selectionSort(aList)
    endTime = time.time()
    print("Selection Sort Completed")	
    conn.send([aList, endTime - startTime])	
    conn.close()
