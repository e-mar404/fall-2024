from queue import PriorityQueue

class Graph:
    def __init__(self, size):
        self.nodes = size + 1
        self.adj_list = {}
        self.path = {}

        for node in range(0, self.nodes):
            self.adj_list[node] = []
            self.path[node] = []

    def add_edges(self, edges):
        for [src, dst, weight] in edges:
            self.adj_list[src].append([dst, weight])

    def set_distance(self):
        dist = {}

        for src in self.adj_list:
            dist[src] = float('inf') 

        return dist

    def reset_path(self, dst):
        self.path[dst] = []

    def track(self, src, dst):
        for visited in self.path[src]:
            self.path[dst].append(visited)

        self.path[dst].append(dst)

    def shortest_path(self, start):
        dist = self.set_distance()
        dist[start] = 0
        self.track(start, start)

        pq = PriorityQueue()
        pq.put((dist[start], start))

        while not pq.empty():
            src = pq.get()[1]
            
            for dst, weight in self.adj_list[src]:
                if(dist[dst] > dist[src] + weight):
                    if (dist[dst] != float('inf')):
                        self.reset_path(dst)

                    self.track(src, dst)

                    dist[dst] = dist[src] + weight
                    pq.put((dist[dst], dst))

        return dist, self.path

    def print_graph(self):
        print('node x can reach [[y, weight], ... , [z, weight]]')

        for node in self.adj_list:
            print('node %s can reach %s' %
                  (node, self.adj_list[node]))

g = Graph(7)
g.add_edges([     
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

g.print_graph()
min_distances, path = g.shortest_path(0)
print('start | goal | shortest distance | path taken')
print(' 0    |  5   |  %-17s| %s' % (min_distances[5], path[5]))
print(' 0    |  6   |  %-17s| %s' % (min_distances[6], path[6]))
print(' 0    |  7   |  %-17s| %s' % (min_distances[7], path[7]))
