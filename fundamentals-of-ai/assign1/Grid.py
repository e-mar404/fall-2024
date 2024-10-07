class Node:
    def __init__(self, coordinates, costX, costY):
        self.coordinates = coordinates
        self.costX = costX
        self.costY = costY
        self.nextX = None
        self.nextY = None
        self.totalCost = float('inf') # f
        self.costToNode = float('inf') # g
        self.heuristic = 0 
    
class Grid:
    def __init__(self):
        self.head = None

    def insertNode(self, coordinates, costX, costY):
        newNode = Node(coordinates, costX, costY) 
        if self.head is None:
            self.head = newNode
            return self.head
        
        x, y = coordinates
        currentNode = self.head
        while (x > 1 and currentNode.nextX):
            currentNode = currentNode.nextX
            x -=1

        while (y > 1 and currentNode.nextY):
            currentNode = currentNode.nextY
            y -= 1
        
        if (x == y):
            if (currentNode.nextX):
                currentNode.nextX.nextY = newNode
                returnNode =currentNode.nextX.nextY
    
            if (currentNode.nextY):
                currentNode.nextY.nextX = newNode
                returnNode = currentNode.nextY.nextX
            return returnNode

        if (x == 1):
            currentNode.nextX = newNode
            returnNode = currentNode.nextX

        if (y == 1):
            currentNode.nextY = newNode
            returnNode = currentNode.nextY

        return returnNode


    def printHelp(self, root):
        if (root == None):
            return

        print('coor: %s, moveX: %s, moveY: %s' %
              (root.coordinates, root.costX, root.costY))
        self.printHelp(root.nextX)
        self.printHelp(root.nextY)


    def printGrid(self):
        self.printHelp(self.head)
