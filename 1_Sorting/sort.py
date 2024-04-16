# -*- coding: utf-8 -*-
# Daniel Głąbicki, 415539
# Niestety nie rozumiem powodu, dla którego moja funkcja quicksort nie zaliczyła testów:
# TestSorting.test_quicksort_is_not_inplace oraz TestSorting.test_quicksort_is_sorted.
# Przecież są podane 2 argumenty pozycyjne.
from typing import List, Set, Dict, Tuple


def quicksort(lst0: List[int], start: int, stop: int) -> List[int]:
    lst: List[int] = lst0[:]
    i: int = start
    j: int = stop
    p: int = lst[(i + j) // 2]
    while i < j:
        while lst[i] < p:
            i += 1
        while lst[j] > p:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
    if start < j:
        quicksort(lst, start, j)
    if i < stop:
        quicksort(lst, i, stop)
    return lst


def bubblesort(lst0: List) -> Tuple[List, int]:
    lst: List[int] = lst0[:]
    l: int = len(lst)
    n: int = 0

    while l > 1:
        is_ordered = True
        for i in range(1, l):
            n += 1
            if lst[i - 1] > lst[i]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
                is_ordered = False
        if is_ordered:
            break
        l -= 1
    return lst, n
