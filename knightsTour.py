from collections import defaultdict

def generateGraph(boardSize):
    knightGraph = defaultdict(list)
    
    for row in range(boardSize):
       for column in range(boardSize):
           #assigns "chess board" space value based on size of board
           nodeId = positionToId(row, column, boardSize)
           possibleMoves = generateLegalMoves(row, column, boardSize)
           
           for m in possibleMoves:
               edgeId = positionToId(m[0], m[1], boardSize)
               knightGraph[nodeId].append(edgeId)
                 
    return knightTour(knightGraph, 0, 0, [], boardSize ** 2)

#to convert row and column position on board to a number
def positionToId(row, column, boardSize):
    return (row * boardSize) + column

#generates possible moves based on the nodes position on the board
def generateLegalMoves(row, column, boardSize):
    moves = []
    possibleMoves = [(-1,-2), (-1,2), (-2,-1), (-2,1),
                   (1,2), (1,-2), (2,1), (2,-1)]
    
    #loops over possible moves adding or subtracting them to the current node position
    for i in possibleMoves:
        newRow = row + i[0]
        newColumn = column + i[1]
        
        #checks if possible moves are valid based on board position
        if legalCoord([newRow, newColumn], boardSize):
            moves.append((newRow, newColumn))
    return moves

def legalCoord(coordinates, boardSize):
    if coordinates[0] >= 0 and coordinates[1] >= 0 and coordinates[0] < boardSize and coordinates[1] < boardSize:
        return True
    return False

#depth first search
def knightTour(knightGraph, position, currentDepth, path, limit):
    knightGraph[position].append('visited')
    path.append(position)
    
    if currentDepth < limit:
        nodesToVisit = knightGraph[position][:-1]
        i = 0
        done = False
        
        while i < len(nodesToVisit) and not done:
            if 'visited' not in knightGraph[nodesToVisit[i]]:
                done = knightTour(knightGraph, nodesToVisit[i], currentDepth + 1, path, limit)
            i += 1
        #remove last inserted node id from path and remove 'visited' from the respective node in the graph
        if not done: 
            path.pop()
            knightGraph[position].pop()
    else:
        done = True
    return done, path, knightGraph

def main():
    done, path, knightGraph = generateGraph(3)
    print('path: ', path)
    print('knight graph: ', knightGraph)
    
main()
    
    