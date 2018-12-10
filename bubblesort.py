# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:40:01 2018

@author: rjenk

CSC 338 Group Project

BubbleSort.py
"""
import random
import numpy as np

# Take a list of elements and sort them using bubble sort
def bubbleSort(dataList):
    length = len(dataList)
    noSwap = False
    while not noSwap:
        swapped = False
        for i in range(1, length):
            if dataList[i - 1] > dataList[i]:
                dataList[i - 1], dataList[i] = dataList[i], dataList[i - 1]
                swapped = True
        --length
        if not swapped:
            noSwap = True


# Main function call to test functionality of bubble sort
def main():
    lst = [i for i in range(100)]
    random.shuffle(lst)
    print(lst)
    bubbleSort(lst)
    print(lst)

if __name__ == "__main__":
    main()
