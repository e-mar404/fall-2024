from queue import PriorityQueue

class Graph:
    def __init__(self, size):
        self.nodes = size + 1
        self.adjList = {}
        self.path = {}

        for node in range(0, self.nodes):
            self.adjList[node] = []
            self.path[node] = []

    def addEdges(self, edges):
        for [src, dst, weight] in edges:
            self.adjList[src].append([dst, weight])

    def setDistance(self):
        dist = {}

        for src in self.adjList:
            dist[src] = float('inf') 

        return dist

    def resetPath(self, dst):
        self.path[dst] = []

    def track(self, src, dst):
        for visited in self.path[src]:
            self.path[dst].append(visited)

        self.path[dst].append(dst)

    def shortestPath(self, start):
        dist = self.setDistance()
        dist[start] = 0
        self.track(start, start)

        pq = PriorityQueue()
        pq.put((dist[start], start))

        while not pq.empty():
            src = pq.get()[1]
            
            for dst, weight in self.adjList[src]:
                if(dist[dst] > dist[src] + weight):
                    if (dist[dst] != float('inf')):
                        self.resetPath(dst)

                    self.track(src, dst)

                    dist[dst] = dist[src] + weight
                    pq.put((dist[dst], dst))

        return dist, self.path

g = Graph(7)
g.addEdges([     
    [0, 1, 2],
    [0, 7, 3],
    [0, 3, 2],
    [1, 4, 4],                 
    [1, 0, 1],
    [3, 0, 1],
    [3, 5, 7],
    [4, 6, 4],
    [5, 6, 2],
    [7, 4, 4],
    [7, 5, 6]])

minDistances, path = g.shortestPath(0)
print('start | goal | shortest distance | path taken')
print(' 0    |  5   |  %-17s| %s' % (minDistances[5], path[5]))
print(' 0    |  6   |  %-17s| %s' % (minDistances[6], path[6]))
print(' 0    |  7   |  %-17s| %s' % (minDistances[7], path[7]))
