#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 11:22:38 2018

@author: martin
"""
import heapq
import sys

def handle_data(lines):
    edges = {}
    start = ''
    for i,line in enumerate(lines):
        
        if line[-2] != ']':
            if line[-2] == ' ':    
                edges[line[:-2]] = {}
            else:
                edges[line[:-1]] = {}

        else:
            
            split = line.split(' [')
            nodes = split[0].split('--')
            edges[nodes[0]][nodes[1]] = int(split[1][0:-2])
            edges[nodes[1]][nodes[0]] = int(split[1][0:-2])
            if start == '':
                start = nodes[0]

    return edges, start

def spanning(edges,s):
    Q = []
    for key in edges[s].keys():
        Q.append([edges[s][key], key, s])
            
    T = []
    heapq.heapify(Q)
    visited = set([s])
    c = 0
    while len(visited) != len(edges):
        entry = heapq.heappop(Q)
        node = entry[1]
        if node not in visited:
            c += 1
            T.append(entry)
            visited.add(node)
            neigh = edges[node].keys()
            for place in neigh:
                if place not in visited:
                    heapq.heappush(Q,[edges[place][node], place, node])
            #sleta efter Qn som får en kortare väg nu
    return T
      
with open(sys.argv[1],'r') as f:
    lines = f.readlines()
    edges, start = handle_data(lines)
Mintree= spanning(edges,start)   
#        
#with open('data/USA-highway-miles.txt','r') as f:
#    lines = f.readlines()
#    edges,start = handle_data(lines)
#Mintree= spanning(edges, start)        
#        
        
#with open('data/tinyEWG-alpha.txt','r') as f:
#    lines = f.readlines()
#    edges = handle_data(lines)
#Mintree= spanning(edges, 'A')
#for key in places.keys():
#    print(key + ' ' + str(places[key]))

length = 0
for i in range(len(Mintree)):
    length = length + Mintree[i][0]
print(length)