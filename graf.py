#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Graph class. Nodes are indexed from 0 to nnodes-1

Created on Tue Feb 27 10:25:18 2018

@author: xpontus
"""

import unittest, random

class Graph:
    """A simple graph class"""
    nnodes = 0
    neighbours = []
    
    def __init__(self, numnodes):
        self.nnodes = numnodes
        self.neighbours = [ [] for i in range(self.nnodes)]
        # functions always return None if end of execution is reached
    
    def addedge(self, i, j):
        if 0 <= i < self.nnodes and 0 <= j < self.nnodes:
            self.neighbours[i].append(j)
            self.neighbours[j].append(i)
        
    def hasedge(self, i, j):
        if 0 <= i < self.nnodes and 0 <= j < self.nnodes:
            assert( (i in self.neighbours[j]) == (j in self.neighbours[i]) )
            return i in self.neighbours[j]
        else:
            return False
    
    def getneighbours(self, i):
        if 0 <= i < self.nnodes:
            return self.neighbours[i]
        else:
            return []
        
    def printedges(self):
        for i in range(self.nnodes):
            print("{}: ".format(i),end='')  # no newline
            if self.neighbours[i]:
                print(*self.neighbours[i], sep=',')
        

# move tests to separate file later
class GraphTest(unittest.TestCase):
    def setup(self): # will be called before any test
        None
    def teardown(self): # will be called after any test
        None
    
    # tests should start w/ test_, they are run in lexicographical order
    def test_graph1(self):
        g = Graph(5)
        g.addedge(0,1)
        g.addedge(0,2)
        g.addedge(0,3)
        g.addedge(0,4)
        self.assertTrue(g.hasedge(0,1))
        self.assertTrue(g.hasedge(0,2))
        self.assertTrue(g.hasedge(0,3))
        self.assertTrue(g.hasedge(0,4))
        self.assertEqual(g.getneighbours(0),[1,2,3,4])  # automatically calls assertListEqual
        self.assertEqual(g.getneighbours(1), [0])
        self.assertEqual(g.getneighbours(2), [0])
        self.assertEqual(g.getneighbours(3), [0])
        self.assertEqual(g.getneighbours(4), [0])

    def testrandomgraphs(self):
        for gno in range(1):
            n = random.randint(30,100)
            g = Graph(n)
            theedges = []
            m = random.randint(n, n*(n-1)//2)
            for mm in range(m):
                a = random.randint(0,n-1)
                b = random.randint(0,n-1)
                theedges.append( (a,b) )  # extra parentheses because tuple
                theedges.append( (b,a) )
                g.addedge(a,b)
            for i in range(n):
                for j in range(n):
                    self.assertEqual(g.hasedge(i,j), (i,j) in theedges)

        
# defined if file is run directly, not if imported 
if __name__ == "__main__":
    unittest.main() # will run all tests found in module
    
    
    
    
