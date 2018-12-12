"""
* Carmen Creswell 
* Group 2
* Insertion Sort 
"""

def insertionSort(alist):
	for i in range(1,len(alist)):
		currentValue = alist[i]
		position = i

		while position > 0 and alist[position - 1] > currentValue:
			alist[position] = alist[position - 1]
			position = position - 1

		alist[position] = currentValue
	return alist
	
def main():
	alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 100, -1, 8, 33, 33, 55, 0, 3, 90, 100000, 4444, -33]
	insertionSort(alist)
	print (alist)

if __name__ == "__main__":
	main()