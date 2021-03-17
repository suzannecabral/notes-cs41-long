class Stack():
    def __init__(self):
        self.storage = []

    def push (self, value):
        self.storage.append(value)

    def pop(self):
        if self.size() > 0:
                return self.storage.pop()
        else:
                return None
    # could also add Stack.peek to see the last item

    def size(self):
        return len(self.storage)

class Queue():
    def __init__(self):
        self.storage = []

    # ... 
    # ...
    # mised some code
    
# usually just import deck and use that
# it's not a list so faster removal
# can implement a queu with a linked list


def island_counter(island_matrix):
    # keep track of the nodes that I have visited
    visited = []

    # build the graph
    for i in range(len(island_matrix)):

        # to make a list with 2 false items:
        # visited.append([False] = 2) 
        visited.append([False] = len(island_matrix[0]))
        # uses the length of the first array

    #create and island counter and initialize it to zero
    island_counter = 0

    # keep traversing the graph, while we still have nodes that we have not visited
    # walk through each cell in the matrix
    for row in range(len(island_matrix)):
        # first row defines cols, like spreadsheet
        for col in range(island_matrix[0]):

            # if the current cell hasn't been visited bfore
            if not visited[row][col]:
                # check if it is a 1
                if island_matrix[row][col] == 1:
                # if so:
                    # do some sort of a traversal, marking each connected node as visited
                    visited = dft(row, col, island_matrix, visited)

                    # increment the island counter by 1
                    island_counter += 1
                    # if we've gotten to this point, we must have found 1

        else:
            # mark the current cell as visited
            visited[row][col] = True

    return island_counter


def dft(row, col, matrix, visited):
    # create an empty stack
    s = Stack()

    # push the starting nodde on to the stack
    # use these like coordinates
    s.push((row, col))
    
    # while the stack is not empty
    while s.size() > 0:
        # pop the first node from the top of the stack
        node = s.pop()
        # row is in [0], col is in [1]
        row = node[0]
        col = node[1]

        # if the node has not been visited before
        if not visited[row][col]:
            # mark the node as visited
            visited[row][col] = True
            # push each (1) neighbor of the node on to the stack
            for neighbor in get_neighbors(row, col, matrix):
                s.push(neighbor)
            # understanding what are neighbors: this is the step that changes with different problems

    # return the visited matrix back to the caller
    return visited


def get_neighbors(row, col, matrix):
    # create an empty list to store neighbors
    neighbors = []

    # check north
    if row > 0 and matrix[row - 1][col] == 1:
    # if we haven't gone out of bounds, 
    # and the thing above us is a 1
        neighbors.append((row-1, col))
        # then we've found a neighbor
        # append the tuple
    # check south
    if row < len(matrix) - 1 and matrix[row + 1][col] == 1:
        neighbors.append((row + 1, col))
    # check east
    if (col < len(matrix[0]) - 1 and matrix[row][col + 1]):
        # ... missed
        pass
    # check west
    if col > 0 and matrix[row][col - 1] == 1:
        #.... missed
        pass
    # return the list of neighbors to the caller


# test code goes below

islands =  [[0, 1, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 0, 0]]


print(island_counter(islands))
# returns 4