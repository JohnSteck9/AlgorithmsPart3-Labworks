
## Tusk - ijones.pdf

## Usage 
    python ijones.py

## Tests 
    python unit_test.py

Approach:

1. The idea is to do Depth First Traversal of given directed graph.
2. Start the DFS traversal from source.
3. Keep storing the visited vertices in an array or HashMap say ‘path[]’.
4. If the destination vertex is reached, print contents of path[].
5. The important thing is to mark current vertices in the path[] as visited also so that the traversal doesn’t go in a cycle.

We’ll consider the worst-case scenario, where the graph is complete, meaning there’s an edge between every pair of vertices. In this case, it turns out the problem is likely to find a permutation of vertices to visit them.

For each permutation of vertices, there is a corresponding path. Hence, the complexity is O(|V|!), where |V| is the number of vertices and |V|! is the factorial of the number of vertices.

This complexity is enormous, of course, but this shouldn’t be surprising because we’re using a backtracking approach.




adjacency_list_view = {
    'a1': {'a3', 'a5', 'a2'},
    'c4': {'a5'},
    'd7': {'e8'},
    'a2': {'a3'},
    'a5': {'b6', 'a3'},
    'e8': {'f9'},
    'a3': {},
    'b6': {},
    'f9': {}
} 