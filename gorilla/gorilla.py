#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 16:33:15 2018

@author: martin
"""

from string import ascii_uppercase
import sys

def fix(lines):
    species=[]
    j = -1
    for i, line in enumerate(lines):
        if line[0] == '>':
            species.append(['',''])
            j += 1
            split = line.split()
            species[j][0]=split[0][1:]
            
        else:
            species[j][1] = ''.join([species[j][1],line])
    return species
    
                    
                
            
        

def Alignment(X,Y,c,alpha):
    m = len(X)
    n = len(Y)
    A = []
    pred = []
    
    #dim(A)=mxn
    for i in range(m+1):
        A.append([])
        pred.append([])
        for j in range(n+1):
            if i == 0:
                A[i].append(j*c[-1][2])
                pred[i].append([i,j-1])
            elif j == 0:
                A[i].append(i*c[2][-1])
                pred[i].append([i-1,j])
            else:
                A[i].append(0)
                pred[i].append([])
            
    for i in range(1,m+1):
        for j in range(1,n+1):
            X_i = X[i-1]
            Y_j = Y[j-1]
            d_ij=c[-1][2]
            a_ij = c[alpha[X_i]][alpha[Y_j]]
            lista = [a_ij+A[i-1][j-1],d_ij+A[i-1][j],d_ij+A[i][j-1]]
            A[i][j] = max(lista)
            if A[i][j] == lista[0]:
                pred[i][j] = [i-1,j-1]
            elif A[i][j] == lista[1]:
                pred[i][j] = [i-1,j]
            else:
                pred[i][j] = [i,j-1]
    string1 = ''
    string2 = ''
    i = m
    j = n
    while pred[i][j][0] !=-1 and pred[i][j][1] !=-1:
        cord = pred[i][j]
        if cord[0] == i:
            string1 = ''.join(['-',string1])
            
            string2 = ''.join([Y[j-1],string2])
        elif cord[1] == j:
            string2 = ''.join(['-',string2])            
            string1 = ''.join([X[i-1],string1])
        else:
            string1 = ''.join([X[i-1],string1])
            string2 = ''.join([Y[j-1],string2])
        
        i = cord[0]
        j = cord[1]

    return A[-1][-1],string1,string2


def alphabet():
    letters = ['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X'] 
    alpha = {letter:index for index,letter in enumerate(letters)}
    return alpha

def c():
     data = [[4,-1,-2,-2,0,-1,-1,0,-2,-1,-1,-1,-1,-2,-1,1,0,-3,-2,0,-2,-1,0,-4],
[-1,5,0,-2,-3,1,0,-2,0,-3,-2,2,-1,-3,-2,-1,-1,-3,-2,-3,-1,0,-1,-4],
[-2,0,6,1,-3,0,0,0,1,-3,-3,0,-2,-3,-2,1,0,-4,-2,-3,3,0,-1,-4],
[-2,-2,1,6,-3,0,2,-1,-1,-3,-4,-1,-3,-3,-1,0,-1,-4,-3,-3,4,1,-1,-4],
[0,-3,-3,-3,9,-3,-4,-3,-3,-1,-1,-3,-1,-2,-3,-1,-1,-2,-2,-1,-3,-3,-2,-4],
[-1,1,0,0,-3,5,2,-2,0,-3,-2,1,0,-3,-1,0,-1,-2,-1,-2,0,3,-1,-4],
[-1,0,0,2,-4,2,5,-2,0,-3,-3,1,-2,-3,-1,0,-1,-3,-2,-2,1,4,-1,-4],
[0,-2,0,-1,-3,-2,-2,6,-2,-4,-4,-2,-3,-3,-2,0,-2,-2,-3,-3,-1,-2,-1,-4],
[-2,0,1,-1,-3,0,0,-2,8,-3,-3,-1,-2,-1,-2,-1,-2,-2,2,-3,0,0,-1,-4],
[-1,-3,-3,-3,-1,-3,-3,-4,-3,4,2,-3,1,0,-3,-2,-1,-3,-1,3,-3,-3,-1,-4],
[-1,-2,-3,-4,-1,-2,-3,-4,-3,2,4,-2,2,0,-3,-2,-1,-2,-1,1,-4,-3,-1,-4],
[-1,2,0,-1,-3,1,1,-2,-1,-3,-2,5,-1,-3,-1,0,-1,-3,-2,-2,0,1,-1,-4],
[-1,-1,-2,-3,-1,0,-2,-3,-2,1,2,-1,5,0,-2,-1,-1,-1,-1,1,-3,-1,-1,-4],
[-2,-3,-3,-3,-2,-3,-3,-3,-1,0,0,-3,0,6,-4,-2,-2,1,3,-1,-3,-3,-1,-4],
[-1,-2,-2,-1,-3,-1,-1,-2,-2,-3,-3,-1,-2,-4,7,-1,-1,-4,-3,-2,-2,-1,-2,-4],
[1,-1,1,0,-1,0,0,0,-1,-2,-2,0,-1,-2,-1,4,1,-3,-2,-2,0,0,0,-4],
[0,-1,0,-1,-1,-1,-1,-2,-2,-1,-1,-1,-1,-2,-1,1,5,-2,-2,0,-1,-1,0,-4],
[-3,-3,-4,-4,-2,-2,-3,-2,-2,-3,-2,-3,-1,1,-4,-3,-2,11,2,-3,-4,-3,-2,-4],
[-2,-2,-2,-3,-2,-1,-2,-3,2,-1,-1,-2,-1,3,-3,-2,-2,2,7,-1,-3,-2,-1,-4],
[0,-3,-3,-3,-1,-2,-2,-3,-3,3,1,-2,1,-1,-2,-2,0,-3,-1,4,-3,-2,-1,-4],
[-2,-1,3,4,-3,0,1,-1,0,-3,-4,0,-3,-3,-2,0,-1,-4,-3,-3,4,1,-1,-4],
[-1,0,0,1,-3,3,4,-2,0,-3,-3,1,-1,-3,-1,0,-1,-3,-2,-2,1,4,-1,-4],
[0,-1,-1,-1,-2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-2,0,0,-2,-1,-1,-1,-1,-1,-4],
[-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,1]]
     return data

alpha = alphabet()
c = c()

#dest = sys.argv[1]
#dest='data/Toy_FASTAs-in.txt'
dest='data/HbB_FASTAs-in.txt'
with open(dest) as file:
    lines = [line.rstrip() for line in file]
    species = fix(lines)
    
result = ''
rat = ['rat','MVHLTDAEKAAVNALWGKVNPDDVGGEALGRLLVVYPWTQRYFDSFGDLSSASAIMGNPKVKAHGKKVINAFNDGLKHLDNLKGTFAHLSELHCDKLHVDPENFRLLGNMIVIVLGHHLGKEFTPCAQAAFQKVVAGVASALAHKYH']
for i in range(len(species)):
    res,string1,string2 = Alignment(species[i][1],rat[1],c,alpha)
    res_string = '--'.join([species[i][0], rat[0]])
    res_string = ': '.join([res_string, str(res)])
    if result == '':
        result = '\n'.join([res_string,string1,string2])
    else:
        result = '\n'.join([result,res_string,string1,string2])
        
print(result)
#with open('res.txt','w') as file:
# file.write(result)
        
        
        












