
import multiprocessing as mp
array = [7,4,1,8,5,2,9,6,3];

def quickSort(start,end):
    if start < end:
        part = partition(start,end)

        quickSort(start,part - 1)
        quickSort(part + 1,end)

def partition(start, end):
    point = array[end - 1]
    i = start
    for j in range(end-1):
        if array[j] <= point:
            i += 1
            temp = array[i + 1]
            array[i] = array[j]
            array[j] = temp
    temp = array[i + 1]
    array[i] = array[end - 1]
    array[end - 1] = temp
    return (i + 1)

def main():
    quickSort(0,len(array))
    print(array)
main()
