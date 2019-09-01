from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

#this class is intended to represent
#the graphical connecting components
class Graph:
      #constructor
      def __init__(self,v):
          #default dictionary to store graph
          self.graph=defaultdict(list)
          #the number of Vertices is a graph
          self.v=v
          #list to store connecting components
          self.cmp=[]
          #l is helping list
          self.l=[]
      #add an edge to graph
      def addEdge(self,u,v):
          self.graph[u].append(v)
      #dfs(depth first search) function
      def DFS(self,v,mark):
          mark[v]=True
          self.l.append(v+1)
          for u in self.graph[v+1]:
              if mark[u-1]==False:
                 self.DFS(u-1,mark)

      #function used for find the
      #connecting component
      def check(self,mark):
          for i in range(self.v):
              if mark[i]==False:
                 self.l.clear()
                 self.DFS(i,mark)
                 self.cmp.append(self.l.copy())


v,e=map(int,input().split())
lst=[]
g=Graph(v)
mark=[False for i in range(v)]

#get graph edges from user
for i in range(e):
    lst.append(tuple(map(int,input().split())))
    g.addEdge(lst[i][0],lst[i][1])
    #because if it were a loop in graph,
    #we wouldn't count twice
    if lst[i][0]!=lst[i][1]:
      g.addEdge(lst[i][1],lst[i][0])


g.check(mark)

for i in g.cmp:
    print(i)

# DFS algorithm :
# the algorithm is executed recursively,
# assuming that all vertices are first
# in the white graph,we consider arbitrary
# vertices such as (r) and start from it.
# first,we black out (r) and then call the
# same algorithm for the neighbors of (r)
#the process of blackening a vertex in the
# following function is modeled by true
#masking that vertex

#see geeksforgeeks for more information