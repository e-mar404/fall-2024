import Grid

g = Grid.Grid()

start = g.insertNode((0, 0), 4, 2)
g.insertNode((1, 0), 3, 1)
g.insertNode((0, 1), 3, 3)
g.insertNode((2, 0), -1, 4)
g.insertNode((1, 1), 4, 2)
g.insertNode((0, 2), 7, -1)
g.insertNode((2, 1), -1, 5)
g.insertNode((1, 2), 1, -1)
g.insertNode((2, 2), -1, 3)
goal = g.insertNode((2, 3), -1, 2)
g.printGrid()
