# -*- coding: utf-8 -*-


# Почти уверен, что лучше встроенного timsort'a на самом python'е не напишешь. Ниже моя попытка реализовать quick sort с небольшой доработкой(медиала из lo, mid, hi), чтобы избежать O(n^2) для отсортированного массива.

def getPivot(a, lo, hi):
    mid = lo + (hi - lo) // 2
    if a[mid] < a[lo]:
        a[lo], a[mid] = a[mid], a[lo]
    if a[hi] < a[lo]:
        a[lo], a[hi] = a[hi], a[lo]
    if a[mid] < a[hi]:
        a[mid], a[hi] = a[hi], a[mid]
    print a[lo], a[mid], a[hi]
    return a[hi]

def partition(a, lo, hi):
    pivot = getPivot(a, lo, hi)
    print a
    print 'pivot:', pivot
    i, j = lo, hi-1
    while True:
        while True:
            if a[i] > pivot or i == hi:
                break
            i += 1
            print 'i:', i
        while True:
            if a[j] < pivot or j == lo:
                break
            j -= 1
            print 'j:', j
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
    a[hi] = a[i]
    a[i] = pivot
    return i

def qsort(a, lo, hi):
    print a
    print a[lo:hi+1]
    if hi - lo <= 0:
        return
    border = partition(a, lo, hi)
    qsort(a, lo, border-1)
    qsort(a, border+1, hi)

