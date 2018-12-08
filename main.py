import time, random, merge, quickSort, InsertionSort
#import for sorts

if __name__ == "__main__":
    size = 2500

    data = [random.randint(0, size) for i in range(size)]    
    mp_bubble_start = time.time()
    #bubble calls
    mp_bubble_elapsed_time = time.time() - mp_bubble_start
    
    mp_insertion_start = time.time()
    #insertion calls
    mp_insertion_elapsed_time = time.time() - mp_insertion_start
    
    mp_quick_start = time.time()
    #quick calls
    mp_quick_elapsed_time = time.time() - mp_quick_start
    
    data = [random.randint(0, size) for i in range(size)]
    mp_merge_start = time.time()
    merge.process_start(data)
    mp_merge_elapsed_time = time.time() - mp_merge_start    
    
    mp_selection_start = time.time()
    #selection calls
    mp_selection_elapsed_time = time.time() - mp_selection_start
    
    bubble_start = time.time()
    #bubble calls
    bubble_elapsed_time = time.time() - bubble_start
    
    data = [random.randint(0, size) for i in range(size)]    
    insertion_start = time.time()
    InsertionSort.serialInsertionSort(data)
    insertion_elapsed_time = time.time() - insertion_start
    
    data = [random.randint(0, size) for i in range(size)]    
    quick_start = time.time()
    quickSort.quickSort(data, 0, len(data)-1)
    quick_elapsed_time = time.time() - quick_start
    
    data = [random.randint(0, size) for i in range(size)]   
    merge_start = time.time()
    merge.sort(data, 0, size-1)
    merge_elapsed_time = time.time() - merge_start    

    selection_start = time.time()
    #selection calls
    selection_elapsed_time = time.time() - selection_start

    print("Time to for multiprocessed bubble sort: ", mp_bubble_elapsed_time)
    print("Time to for multiprocessed insertion sort: ", mp_insertion_elapsed_time)
    print("Time to for multiprocessed quick sort: ", mp_quick_elapsed_time)
    print("Time to for multiprocessed merge sort: ", mp_merge_elapsed_time)
    print("Time to for multiprocessed selection sort: ", mp_selection_elapsed_time)
    print("Time to for bubble sort: ", bubble_elapsed_time)
    print("Time to for insertion sort: ", insertion_elapsed_time)
    print("Time to for quick sort: ", quick_elapsed_time)
    print("Time to for merge sort: ", merge_elapsed_time)
    print("Time to for selection sort: ", selection_elapsed_time)
