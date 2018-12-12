import time 

# Serial Insertion Sort 
# Slightly modified from: http://interactivepython.org/
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location
               print(positionOfMax)
               print(alist[positionOfMax])
       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
