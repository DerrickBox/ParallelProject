import math, random
import multiprocessing as mp

def process_start(a):
    q = mp.Queue()
    processes = []
    results = []
    checklist = []

    upivot(a,processes,q)
    
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    while not q.empty():
        checklist.append(q.get())

    for i in range(len(checklist)-1):
        if checklist[i-1] < checklist[i]:
            results += checklist[i-1]
            results += checklist[i]
        else:
            results += checklist[i]
            results += checklist[i-1]
            
    return results

def upivot(a, processes, q):
    p1list = []
    p2list = []
    pivot = a[math.floor(len(a)/2)]    
    for ele in a:
        if ele > pivot:
            p2list.append(ele)
        elif ele < pivot or ele == pivot:
            p1list.append(ele)

    p1 = mp.Process(target=mpsort, args=[p1list, 0, len(p1list)-1, q])  
    processes.append(p1)    
    p2 = mp.Process(target=mpsort, args=[p2list, 0, len(p2list)-1, q])  
    processes.append(p2)

def sort(a, left, right):
    if (left >= right):
        return

    center = math.floor((left+right)/2)
    sort(a, left, center)
    sort(a, center+1, right)
    merge(a, left, right, center)

    return a

def mpsort(a, left, right, q):
    if (left >= right):
        return

    center = math.floor((left+right)/2)
    sort(a, left, center)
    sort(a, center+1, right)
    merge(a, left, right, center)
    q.put(a)

def merge(a, left, right, center):
    n1 = center - left + 1
    n2 = right - center 
    leftarr = [0]*n1
    rightarr = [0]*n2
  
    for i in range(0 , n1): 
        leftarr[i] = a[left + i] 
  
    for j in range(0 , n2): 
        rightarr[j] = a[center + 1 + j] 
  
    i,j,leftStart = 0,0,left
  
    while i < n1 and j < n2 : 
        if leftarr[i] <= rightarr[j]: 
            a[leftStart] = leftarr[i] 
            i += 1
        else: 
            a[leftStart] = rightarr[j] 
            j += 1
        leftStart += 1

    while i < n1: 
        a[leftStart] = leftarr[i] 
        i += 1
        leftStart += 1
  
    while j < n2: 
        a[leftStart] = rightarr[j] 
        j += 1
        leftStart += 1

if __name__ == "__main__":
    size = 2500
    
    data = [random.randint(0, size) for i in range(size)]
    print(data)
    sort(data, 0, len(data)-1)
    print(data)
    
    data = [random.randint(0, size) for i in range(size)]
    print(data)
    print(process_start(data))
