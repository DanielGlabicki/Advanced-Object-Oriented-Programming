#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Set, Dict, NamedTuple
from enum import Enum, auto
import networkx as nx
 
# Pomocnicza definicja podpowiedzi typu reprezentującego etykietę
# wierzchołka (liczba 1..n).
VertexID = int
EdgeID = int
# Pomocnicza definicja podpowiedzi typu reprezentującego listę sąsiedztwa.
AdjList = Dict[VertexID, List[VertexID]]
 
Distance = int


class Colour(Enum):
    WHITE = auto()
    GREY = auto()
    BLACK = auto()


def neighbors(adjlist: AdjList, start_vertex_id: VertexID,
              max_distance: Distance) -> Set[VertexID]:
    return_list = []
    adjlist2 = {}
    for k, v in adjlist.items():
        adjlist2[k] = ([Colour.WHITE, 0], v)
    adjlist2[start_vertex_id][0][0] = Colour.GREY
    q = [start_vertex_id]
    while q:
        vertex_id = q.pop(0)
        vertex_distance = adjlist2[vertex_id][0][1] + 1
        if vertex_distance > max_distance:
            break
        for v in adjlist2[vertex_id][1]:
            return_list.append(v)
            if v in adjlist:
                if adjlist2[v][0][0] == Colour.WHITE:
                    adjlist2[v][0][0] = Colour.GREY
                    adjlist2[v][0][1] = vertex_distance
                    q.append(v)
                else:
                    adjlist2[v] = ([Colour.GREY, vertex_distance], [])
        adjlist2[vertex_id][0][0] = Colour.BLACK
    return set(return_list)


def load_multigraph_from_file(filepath: str) -> nx.MultiDiGraph:
    """Stwórz multigraf na podstawie danych o krawędziach wczytanych z pliku.

    :param filepath: względna ścieżka do pliku (wraz z rozszerzeniem)
    :return: multigraf
    """
    g = nx.MultiDiGraph()
    with open(filepath, 'r') as f:
        text = ""
        for line in f:
            text += line
    data = text.split()
    for i in range(len(data)):
        data[i].strip()
        data[i] = float(data[i])
    data2 = []
    for i in range(0, len(data), 3):
        data2.extend([(data[i], data[i + 1], data[i + 2])])
    g.add_weighted_edges_from(data2)
    return g


# Nazwana krotka reprezentująca segment ścieżki.
class TrailSegmentEntry(NamedTuple):
    v_start: VertexID
    v_end: VertexID
    edge: EdgeID
    weight: float


Trail = List[TrailSegmentEntry]


def find_min_trail(g: nx.MultiDiGraph, v_start: VertexID, v_end: VertexID) -> Trail:
    """Znajdź najkrótszą ścieżkę w grafie pomiędzy zadanymi wierzchołkami.

    :param g: graf
    :param v_start: wierzchołek początkowy
    :param v_end: wierzchołek końcowy
    :return: najkrótsza ścieżka
    """
    trail = []
    dijkstra_path_nodes = nx.dijkstra_path(g, v_start, v_end)
    for i in range(len(dijkstra_path_nodes[:-1])):
        list_of_weights = []
        for k in range(len(g[dijkstra_path_nodes[i]][dijkstra_path_nodes[i + 1]])):
            list_of_weights.append(g[dijkstra_path_nodes[i]][dijkstra_path_nodes[i + 1]][k]['weight'])
        min_index = list_of_weights.index(min(list_of_weights))
        # min_index - to równocześnie optymalna krawędź
        trail.append(TrailSegmentEntry(dijkstra_path_nodes[i], dijkstra_path_nodes[i + 1], min_index,
                                       g[dijkstra_path_nodes[i]][dijkstra_path_nodes[i + 1]][min_index]['weight']))
    # ALTERNATYWNIE:
    # for i in dijkstra_path_nodes[:-1]:
    #     best_edge = 0  # mało optymalne
    #     weight = g[i][j][0]['weight']
    #     for k in range(1, len(g[i][j])):
    #         if weight > g[i][j][k]['weight']:
    #             best_edge = k
    #             weight = g[i][j][k]['weight']
    #     trail.extend(TrailSegmentEntry(i, j, best_edge, weight))

    return trail


def trail_to_str(trail: Trail) -> str:
    """Wyznacz reprezentację tekstową ścieżki.

    :param trail: ścieżka
    :return: reprezentacja tekstowa ścieżki
    """
    trail_str = str(int(trail[0].v_start))
    sum_of_weights = 0
    for i in range(len(trail)):
        sum_of_weights += trail[i].weight
        trail_str += " -[{0}: {1}]-> {2}".format(int(trail[i].edge), trail[i].weight, int(trail[i].v_end))
    return trail_str + "  (total = {})".format(sum_of_weights)

# graph = nx.MultiDiGraph()
# graph.add_weighted_edges_from([(1, 3, 0.2)])
# graph.add_weighted_edges_from([(1, 2, 0.5)])
# graph.add_weighted_edges_from([(2, 3, 0.4)])
# graph.add_weighted_edges_from([(2, 3, 0.3)])
# graph.add_weighted_edges_from([(2, 4, 0.3)])
# graph.add_weighted_edges_from([(2, 4, 0.3)])
# graph.add_weighted_edges_from([(4, 5, 0.1)])
# graph.add_weighted_edges_from([(5, 3, 0.1)])
# graph.add_weighted_edges_from([(3, 5, 0.2)])
# graph.add_weighted_edges_from([(5, 6, 0.2)])
# # g = load_multigraph_from_file('dgb.dat')
# print(graph)
# x = find_min_trail(graph, 1, 6)
# print(x)
# s = trail_to_str(x)
# print(s)

# Daniel Głąbicki, 415539
