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
	
def main():
	

	alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 100, -1, 8, 33, 33, 55, 0, 3, 90, 100000, 4444, -33]
	print("Unsorted:", alist)

	startTime = time.time()
	selectionSort(alist)
	endTime = time.time()
	totalTime = endTime - startTime

	print("Serial Sorted:", alist)
	print("Execution time: {} seconds".format(totalTime))
		
	
if __name__ == "__main__":
    main()