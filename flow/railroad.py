#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 19:15:22 2018

@author: martin
"""
#P simple path through graph, b smallest residual edge capacity, edge on p
#graph = [nodes]
#nod = [index,name,[[from,capacity]],[[to,capacity]]]
import sys

class node:
    
    def __init__(self,name, num):
        self.name = name
        self.forward = []
        self.backward = []
        self.arc = [0]*num #alla grannar med C värden, initiera forward = arc
        
def augment(graph,Gf, P, s,t):
    b = float('inf')
    i = t
    while P[i][0] != None:
        node = P[i]
        if node[1] < b and node[1] !=-1:
            b = node[1]
        i = P[i][0]
    i = t
    while i != s:
        node = P[i]
        if node[2] == 'f':
            graph[node[0]][i] += b
        elif node[2] == 'b':
            graph[i][node[0]] -= b
        i = node[0]
    return sum(graph[s]),graph
            
# vi initierar grafen så att forward = arc
def max_flow(Gf,s,t):
    graph = []
    num = len(Gf)
    f = 0
    for i in range(num):
        graph.append([])
        for j in range(num):
            graph[i].append(0)
            
    switch,path = BFS(Gf,s,t)
    while switch[t]:
        fp, graph = augment(graph,Gf,path,s,t)
        for i in range(num):
            Gf[i].forward = []
            Gf[i].backward = []
            for j in range(num):
                c = Gf[i].arc[j]
                if c != 0:
                    res = graph[i][j]
                    if c == -1:
                        c = 10000
                    if c-res > 0:
                        Gf[i].forward.append([j,c-res])
                    if res > 0:
                        Gf[i].backward.append([j,res])
        switch, path = BFS(Gf, s, t)
    return graph, sum(graph[s]), Gf
                    
        
        
def parse(lines):
    num = int(lines[0])
    Gf = []
    for i in range(1,1+num):
        line = lines[i]
        Gf.append(node(lines[i],num))
        if line == 'ORIGINS':
            s = i-1
        if line == 'DESTINATIONS':
            t = i-1
    m = int(lines[num+1])
    for i in range(num+2,num+2+m):
        split = lines[i].split()
        for i in range(3):
            split[i] = int(split[i])
        Gf[split[0]].arc[split[1]] = split[2]
        Gf[split[0]].forward.append([split[1],split[2]])
        Gf[split[1]].arc[split[0]] = split[2]
        Gf[split[1]].forward.append([split[0],split[2]])
        
    return Gf,s,t
        
                
        
def min_cut(Gf,visited):
    cut = []
    for i, val in enumerate(visited):
        
        if val:
            for j, val2 in enumerate(Gf):
                if not visited[j] and val2.arc[i] !=0:
                    cut.append([i, j, val2.arc[i]])
    return cut
                                            
    
def BFS(Gf, s, t):
 
    visited =[False]*len(Gf)
    path = [None]*len(Gf)
    queue=[]
    queue.append(s)
    visited[s] = True
    
    path[s] = [None,None,None]
    i = 0
    # Standard BFS Loop
    while queue:
        i +=1
        u = queue.pop()
        for ind, nesta in enumerate(Gf[u].forward):
            if not visited[nesta[0]] and (nesta[1] > 0 or nesta[1] == -1):
                queue.append(nesta[0])
                visited[nesta[0]] = True
                path[nesta[0]] = [u,nesta[1],'f']
                    
#        for ind, nesta in enumerate(Gf[u].backward):
#            if not visited[nesta[0]] and nesta[1] > 0:
#                queue.append(nesta[0])
#                visited[nesta[0]] = True
#                path[nesta[0]] = [u,nesta[1],'b']
    return visited, path

dest = 'data/rail2.txt'
#dest = sys.argv[1]
with open(dest) as file:
    lines = [line.rstrip() for line in file]
    railway,s,t = parse(lines)
path = BFS(railway, s, t)
graph, f, Gf= max_flow(railway,s,t)
visited, p = BFS(Gf,s,t)
cut = min_cut(Gf,visited)
for i, val in enumerate(cut):
    val = list(map(str,val))
    s = ' '.join(val)
    print(s)
print(f)
