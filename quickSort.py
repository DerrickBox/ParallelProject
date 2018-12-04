import multiprocessing as mp
import threading as thr

def quickSort(array,start,end):
    if start < end:
        part = partition(array, start,end)
        quickSort(array,start,part - 1)
        quickSort(array,part + 1,end)

def partition(array,start, end):
    point = array[end]
    i = start - 1
    for j in range(start, end):
        if array[j] <= point:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    temp = array[i + 1]
    array[i + 1] = array[end]
    array[end] = temp
    return (i + 1)

def main():
    array = [7, 23, 24, 3, 12, 32, 31, 11, 25, 2, 17, 28, 14, 21, 30, 33, 37, 5, 29, 26, 27, 4, 10, 8, 20, 22, 13, 34, 35, 9, 39, 16, 38, 19, 6, 40, 15, 1, 36, 18]
    quickSort(array,0,len(array)-1)
    print(array)
main()
