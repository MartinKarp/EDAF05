F#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 12:42:49 2018

@author: martin
"""

#nodklass
#lista med grannar
#sin predecesor
#ett namn
import sys
from collections import deque
import time
#
#class nod:
#    
#    def __init__(self,name,neighbors):
#        self.name = name
#        self.neighbors = neighbors

#skapa hashmap med massa noder. nyckel deras namn och värde noden. 
#Något fel här, great länkar inte till earth.        
def create_Dict(words):
    nodes = {}
    for word in words:
        node = []
        for key in nodes.keys():
            last4 = list(word[1:])
            letters = list(key) 
            last42 = list(key[1:])
            letters2 = list(word)
        
            for i in range(4):
                for j in range(len(letters)):
                    if letters[j] == last4[i]:
                        del letters[j]
                        break
            
                for j in range(len(letters2)):
                    if letters2[j] == last42[i]:
                        del letters2[j]
                        break
            if len(letters) == 1:
                node.append(key)
            if len(letters2) == 1:
                nodes[key].append(word)

        nodes[word] = node
    return nodes
    


def BFS(Nodes,s,t):
    
    if s == t:
        return 0
    
    q = deque()
    q.append(s)
    visited = {}
    visited[s] = True
    pred = {}
    while len(q) != 0:
        v = q.popleft()
        for w in Nodes[v]:
    
            if visited.get(w) == None:
                visited[w] = True
                q.append(w)
                pred[w] = v
                if w == t:
                    n = 0
                    name = w
                    #names = name
                    while name != s:
                        n +=1
                        name = pred[name]
                        #names = ' '.join([names,name])
                    return n
    return -1

t =time.clock()
with open(sys.argv[1],"r") as f:
    data = f.read()
    data = data.split()
    Nodes = create_Dict(data)
#print(time.clock()-t)
t = time.clock()
with open(sys.argv[2],'r') as f:
    data = f.read()
    data = data.split()
    for i in range(int(len(data)/2)):
        print(BFS(Nodes,data[2*i],data[2*i+1]))

#print(time.clock()-t)
#with open("data/words-50.txt","r") as f:
#    data = f.read()
#    data = data.split()
#    Nodes = create_Dict(data)
#
#with open("data/words-50-in.txt",'r') as f:
#    data = f.read()
#    data = data.split()
#    for i in range(int(len(data)/2)):
#        print(BFS(Nodes,data[2*i],data[2*i+1]))
        
    
