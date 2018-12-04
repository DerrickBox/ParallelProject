import multiprocessing as mp
import threading as thr

def quickSort(array,start,end,threads):
    if start < end:
        part = partition(array, start,end)

        t = thr.Thread(target = quickSort, args = [array,start,part - 1,threads])
        t = thr.Thread(target = quickSort, args = [array,part + 1,end,threads])
        threads.append(t)
        t.start()

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
    threads = []
    array = [7, 23, 24, 3, 12, 32, 31, 11, 25, 2, 17, 28, 14, 21, 30, 33, 37, 5, 29, 26, 27, 4, 10, 8, 20, 22, 13, 34, 35, 9, 39, 16, 38, 19, 6, 40, 15, 1, 36, 18]
    t = thr.Thread(target = quickSort, args = [array,0,len(array)-1,threads])
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    print(array)
main()
