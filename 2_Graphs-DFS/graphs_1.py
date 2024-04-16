#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from typing import List, Dict
from collections import defaultdict


def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    adjlist = defaultdict(list)
    for i in range(len(adjmat)):
        for j in range(len(adjmat[i])):
            for k in range(adjmat[i][j]):
                adjlist[i + 1].append(j + 1)
    return adjlist


def dfs_recursive(G: Dict[int, List[int]], s: int, visited: List[int] = None) -> List[int]:
    if visited is None:
        visited = []
    visited.append(s)
    for u in G[s]:
        if u in G:
            if u not in visited:
                dfs_recursive(G, u, visited)
        elif u not in visited:
            visited.append(u)
    return visited


def dfs_iterative(G: Dict[int, List[int]], s: int) -> List[int]:
    stack = [s]
    visited = []
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            if v in G:
                for u in reversed(G[v]):
                    stack.append(u)
    return visited


def tej_funkcji_nie_ma_w_szkielecie_ale_musi_byc(G: Dict[int, List[int]], s: int, visited: List[int] = None) -> bool:
    # sprawdza cykliczność
    if visited is None:
        visited = []
    visited.append(s)
    if s in G:
        for ver in G[s]:
            if ver in visited:
                return True
            elif tej_funkcji_nie_ma_w_szkielecie_ale_musi_byc(G, s + 1, visited[:]):
                return True
    return False


def is_acyclic(G: Dict[int, List[int]]) -> bool:
    for ver in G:
        if tej_funkcji_nie_ma_w_szkielecie_ale_musi_byc(G, ver):
            return False
    return True

# Daniel Głąbicki, 415539
