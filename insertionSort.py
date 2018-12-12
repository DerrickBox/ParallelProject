"""
* Carmen Creswell 
* Group 2
* Insertion Sort 
"""
import time 	
import multiprocessing as mp

numProc = 4 # Starting number of Processes

def insertionSort(alist):
	for i in range(1,len(alist)):
		currentValue = alist[i]
		position = i

		while position > 0 and alist[position - 1] > currentValue:
			alist[position] = alist[position - 1]
			position = position - 1

		alist[position] = currentValue
	return alist
	
def multiInsertionSort(conn, alist):	
    startTime = time.time()	
    alist = insertionSort(alist)	
    endTime = time.time()	
    print("Insertion Sort Completed")	
    conn.send([alist, endTime - startTime])	
    conn.close()
	
def main():
	startTime = time.time()
	alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 100, -1, 8, 33, 33, 55, 0, 3, 90, 100000, 4444, -33]
	print("Unsorted:", alist)	
		
	serialSortedList = insertionSort(alist)	
	endTime = time.time()	
	totalTime = endTime - startTime	
		
	print("Serial Sorted:", serialSortedList)	
	print("Execution time: {} seconds".format(totalTime))	
 	# Multiprocessing Calls	
	"""	
    processes = []	
	for i in range(numProc):	
		p = mp.Process(target = multiInsertionSort, args = [alist,])	
		processes.append(p)	
		
	for p in processes: 	
		p.start()	
	for p in processes: 	
		p.join()	
		
	#print("Multiprocessing Sorted:", multiSortedList)
	"""

if __name__ == "__main__":
	main()