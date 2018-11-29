"""
* Carmen Creswell 
* Group 2
* Insertion Sort 
"""

import time 
import multiprocessing as mp

numProc = 4 #	Starting number of Processes

# Serial Insertion Sort 
# Slightly modified from: http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
def serialInsertionSort(alist):
	for index in range(1,len(alist)):
		currentvalue = alist[index]
		position = index

		while position > 0 and alist[position - 1] > currentvalue:
			alist[position] = alist[position - 1]
			position = position - 1

		alist[position] = currentvalue
	return alist
	
def multiInsertionSort(alist): 
	for index in range(1,len(alist)):
		currentvalue = alist[index]
		position = index

		while position > 0 and alist[position - 1] > currentvalue:
			alist[position] = alist[position - 1]
			position = position - 1

		alist[position] = currentvalue
	return alist

def main():
	startTime = time.time()
	# Serial Calls
	alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 100, -1, 8, 33, 33, 55, 0, 3, 90, 100000, 4444, -33]
	print("Unsorted:", alist)
	
	serialSortedList = serialInsertionSort(alist)
	endTime = time.time()
	totalTime = endTime - startTime
	
	print("Serial Sorted:", serialSortedList)
	print("Execution time: {} seconds".format(totalTime))

	# Multiprocessing Calls
	processes = []
	for i in range(numProc):
		p = mp.Process(target = multiInsertionSort, args = [alist,])
		processes.append(p)
	
	for p in processes: 
		p.start()
	for p in processes: 
		p.join()
	
	#print("Multiprocessing Sorted:", multiSortedList)
		
	
if __name__ == "__main__":
    main()