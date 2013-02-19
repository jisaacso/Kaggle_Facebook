from numpy import *
from scipy import sparse
import os
import csv
import pickle
import Queue

def uniformsearch(snode,enode):
    global S
    frontier = PriorityQueue()
    node = snode
    frontier.put(node)
    cost = 0
    explored = array([False]*len(S))

    while True:
        if frontier.empty():
            return -1
        node = frontier.pop()
        if node == enode:
            return cost
        explored[node]=True
        nhbrs = A[node,:].nonzero()
        nhbrs = nhbrs[1]
        if not nhbrs:
            #dosomething
        for nhbr in nhbrs:
            if explored[nhbr]==False:
                if frontier.
                
            
            
            


if __name__ == '__main__':
    

    global S

    EPS = .0000001

    MAX_NUM_NODES = 30000
    A = sparse.dok_matrix((MAX_NUM_NODES,MAX_NUM_NODES))
    S = A

    with open('train-all-clean-hashed.txt', 'rb') as csvfile:
        adjreader = csv.reader(csvfile, delimiter="|")

        for row in adjreader:
            if row[0]!='train1.txt':
                break
            A[int(row[1]),int(row[2])]=int(row[3])+EPS

#        dj = sparse.csgraph.dijkstra(A,directed=True)


    with open('paths-clean-hashed.txt','rb') as pathfile:
        pathreader = csv.reader(pathfile,delimiter="|")
        idx = -1
        for ASpath in pathreader:
            idx+=1
            ASCount = len(ASpath)
            if ASCount==1:
                isoptimalvec.append(1)
                continue
            pathlength = 0
            for ASidx in range(1,ASCount):
                pathlength += A[ASpath[ASidx-1]][ASpath[ASidx]]
 
            #if pathlength == 0, path optimal...set 
            if pathlength == ASCount*EPS:
                isoptimalvec.append(1)
                continue
            #if pathlength > 0, find optimal path at t0
            minpath = uniformsearch(ASpath[0],ASpath[-1])
            if minpath !=-1 and minpath < pathlength:
                isoptimalvec.append(0)
            elif minpath !=-1 and minpath >=pathlength:
                isoptimalvec.append(1)
            else:
                print 'ut oh minpath == -1'
            print float(idx)/10000.0
        pickle.dump(isoptimalvec,open('optimalvec.pkl','wb'))
