#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 11:22:38 2018

@author: martin
"""
import heapq
import sys
from collections import deque

def handle_data(lines):
    places = {}
    string = ''
    edges = []
    for i,line in enumerate(lines):
        
        if line[-2] != ']':
            if line[-2] == ' ':    
                places[line[:-2]] = i
            else:
                places[line[:-1]] = i

        else:
            if len(edges) == 0:
                for i in range(len(places)):
                    edges.append([0 for j in range(i+1)])

            split = line.split(' [')
            nodes = split[0].split('--')
            nod1 = places[nodes[0]]
            nod2 = places[nodes[1]]
            if nod1 > nod2:    
                edges[nod1][nod2] = int(split[1][0:-2])
            else:
                edges[nod2][nod1] = int(split[1][0:-2])
    return places, edges

def spanning(places, edges,s):
    Q = []
    index_s = places[s]
    for key in places.keys():
        i= places[key]
        if index_s > i:
            ds = edges[index_s][i]
        else:
            ds = edges[i][index_s]
        if ds != 0:
            Q.append([ds, key, s])
        elif ds == 0 and key == s:
            Q.append([ds, key, s])
        else:
            Q.append([sys.maxint, key, s])
            
    T = []
    heapq.heapify(Q)
    visited = set([s])
    while len(Q) != 0:
        entry = heapq.heappop(Q)
        node = entry[1]
        if node not in visited:
            T.append(entry)
            visited.add(node)
            i_n = places[node]
            for key in places.keys():
                i_k = places[key]
                if i_k > i_n:   
                    dist = edges[i_k][i_n]
                else:
                    dist = edges[i_n][i_k]
                if key not in visited and dist != 0:
                    heapq.heappush(Q,[dist, key, node])
        #sleta efter Qn som får en kortare väg nu
    return T
      
with open(sys.argv[1],'r') as f:
    lines = f.readlines()
    places, edges = handle_data(lines)
Mintree= spanning(places, edges, places.keys()[0])   
        
#with open('data/USA-highway-miles.txt','r') as f:
#    lines = f.readlines()
#    places, edges = handle_data(lines)
#Mintree= spanning(places, edges, 'Williamson')        
        
        
#with open('data/tinyEWG-alpha.txt','r') as f:
#    lines = f.readlines()
#    places, edges = handle_data(lines)
#Mintree= spanning(places, edges, 'A')
#for key in places.keys():
#    print(key + ' ' + str(places[key]))

length = 0
for i in range(len(Mintree)):
    length = length + Mintree[i][0]
print(length)