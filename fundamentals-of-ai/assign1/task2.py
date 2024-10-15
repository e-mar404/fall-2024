import heapq

class Cell:
    def __init__(self, cost_x, cost_y):
        self.cost_x = cost_x
        self.cost_y = cost_y
        self.parent_x = 0
        self.parent_y = 0
        self.f = float('inf')
        self.g = float('inf')
        self.heuristic = 0 
    
class Grid:
    def __init__(self, N):
        self.N = N + 1
        self.grid = [[-1 for _ in range(self.N)] for _ in range(self.N)]

    def add_cell(self, coordinates, cost_x, cost_y):
        cell = Cell(cost_x, cost_y)
        
        col, row = coordinates
        self.grid[row][col] = cell

    def is_inbound(self, position):
        col, row = position

        return  ((col < self.N and col >= 0) and
                (row < self.N and row >= 0))

    def is_available(self, position):
        col, row = position

        return self.grid[row][col] != -1

    def heuristic_value(self, position, goal):
        cur_col, cur_row = position
        goal_col, goal_row = goal

        return ((cur_col - goal_col) ** 2 + (cur_row - goal_row) ** 2) ** 0.5 

    def at_destination(self, position, goal):
        return position == goal

    def trace_route(self, goal):
        path = []
        col, row = goal

        while not (self.grid[row][col].parent_x == col and
                   self.grid[row][col].parent_y == row):
            path.append((col, row))

            temp_col = self.grid[row][col].parent_x                                    
            temp_row = self.grid[row][col].parent_y
            col = temp_col
            row = temp_row

        path.append((col, row))
        path.reverse()

        print('(start) ->',  end=' ')
        for step in path:
            print(step, '->', end=' ')
        print('(end)')
        

    def astar(self, start, goal):
        visited = [[False for _ in range(self.N)] for _ in range(self.N)]

        start_col, start_row = start
        start_cell = self.grid[start_row][start_col]
        start_cell.f = 0
        start_cell.g = 0
        start_cell.paren_x = start_col 
        start_cell.parent_y = start_row

        queue = []
        heapq.heappush(queue, (0.0, (start)))

        while len(queue) > 0:
            _, (cur_col, cur_row) = heapq.heappop(queue)
            visited[cur_row][cur_col] = True
            cur_cell = self.grid[cur_row][cur_col]

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for x, y in directions:
                backwards = False
                new_col = cur_col + x 
                new_row = cur_row + y 

                if (not self.is_inbound((new_col, new_row))):
                    continue

                new_cell = self.grid[new_row][new_col]


                if (self.is_available((new_col, new_row))):
                    print(f'looking at {new_col} {new_row}')

                    if (x == 1):
                        cost = cur_cell.cost_x
                    elif (x == -1):
                        cost = new_cell.cost_x
                        backwards = True

                    if (y == 1):
                        cost = cur_cell.cost_y
                    elif (y == -1):
                        cost = new_cell.cost_y
                        backwards = True

                    if (cost == -1):
                        continue

                    new_g = cur_cell.g + cost
                    new_h = self.heuristic_value((new_row, new_col), goal)
                    new_f = new_g + new_h
                    
                    if (self.at_destination((new_col, new_row), goal)):
                        new_cell.f = new_f
                        new_cell.g = new_g
                        new_cell.h = new_h
                        new_cell.parent_x = new_col if backwards else cur_col
                        new_cell.parent_y = new_row if backwards else cur_row

                        print('path found after performing astar: (with cost of %s):' %
                              new_cell.g)

                        self.trace_route(goal)

                        return


                    if (new_cell.f == float('inf') or new_cell.f > new_f):
                        heapq.heappush(queue, (new_f, (new_col, new_row)))

                        new_cell.f = new_f
                        new_cell.g = new_g
                        new_cell.h = new_h
                        new_cell.parent_x = cur_col
                        new_cell.parent_y = cur_row
        return

    def at(self, position):
        col, row = position
        if self.grid[row][col] != -1:
            return f'cost_x: {self.grid[row][col].cost_x}, cost_y: {self.grid[row][col].cost_y}'
        return '-1'

    def print_grid(self):
        print('using grid:')
        for row in range(self.N):
            print('[', end='')
            for col in range(self.N):
                print('%-22s' % self.at((col, row)), end=', ')
            print(']')

    def clear(self):
        self.grid = [[-1 for _ in range(self.N)] for _ in range(self.N)]



g = Grid(3)

'''
g.add_cell((0, 0), 4, 2)
g.add_cell((1, 0), 3, 1)
g.add_cell((0, 1), 3, 3)
g.add_cell((2, 0), -1, 4)
g.add_cell((1, 1), 4, 2)
g.add_cell((0, 2), 7, -1)
g.add_cell((2, 1), -1, 5)
g.add_cell((1, 2), 1, -1)
g.add_cell((2, 2), -1, 3)
g.add_cell((2, 3), -1, -1)

g.print_grid()
g.astar((0, 0), (2,3))

g.clear()
g.add_cell((0, 0), 1, 9)
g.add_cell((1, 0), -1, 1)
g.add_cell((0, 1), 1, 1)
g.add_cell((1, 1), 9, 9)
g.add_cell((0, 2), 9, 1)
g.add_cell((2, 1), -1, 1)
g.add_cell((1, 2), 9, 9)
g.add_cell((0, 3), 1, -1)
g.add_cell((2, 2), 1, 1)
g.add_cell((1, 3), 1, -1)
g.add_cell((3, 2), -1, 1)
g.add_cell((2, 3), -1, -1)
g.add_cell((3, 3), -1, -1)

g.print_grid()
g.astar((0, 0), (3, 3))
'''

g.clear()
g.add_cell((0, 0), 1, 9)
g.add_cell((1, 0), -1, 1)
g.add_cell((0, 1), 1, 1)
g.add_cell((1, 1), 9, 9)
g.add_cell((0, 2), 9, 1)
g.add_cell((2, 1), -1, 9)
g.add_cell((1, 2), 1, 1)
g.add_cell((0, 3), 1, -1)
g.add_cell((2, 2), -1, -1)
g.add_cell((2, 3), -1, -1)

g.print_grid()
g.astar((0, 0), (2,2))
