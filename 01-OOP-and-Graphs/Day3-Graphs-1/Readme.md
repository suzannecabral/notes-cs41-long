# Graphs

- graphs have nodes and edges
- traversal is like searching a map of rooms in adventure game
- relationships: user is node, friendship is the edge (two ways)
- twitter follow edge - is a one-way interaction
- google maps: locations = nodes, routes = edges

## Islands Problem

1s are islands, 0 are water
diagonals are not connected

depth first traversal
if you've done depth first traversal, can do any depth first traversal
same with breadth first

1. keep track of nodes that you've visited
2. build the graph
3. create an island counter and initizlise it to zero
4. keep traverising the graph while we still have unvisited nodes
5. walk through each cell in th atrix
    a. if the current cell has not been visited:
        i. check if it is a 1
        ii. do a traversal marking each connected node as visited
        iii. increment the island counter by 1

make it like a spreadsheet, treat it like cols and rows

refer to functions before you make them