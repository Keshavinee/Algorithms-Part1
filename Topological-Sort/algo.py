class Graph:
    def __init__(self,v,e):
        self.v = v
        self.e = e

        # adjacency matrix
        self.adj = [[0 for i in range(self.v)] for j in range(self.v)]

        for edge in range(self.e):
            a, b = [int(j) for j in input().split()]
            self.adj[a][b] = 1

    def topologicalSortHelper(self, visited, u, stack):
        visited[u] = 1

        for v in range(self.v):
            if (not visited[v]) and (self.adj[u][v]):
                stack = self.topologicalSortHelper(visited, v, stack)
        stack.append(u)
        return stack

    def topologicalSort(self):
        visited = [0 for i in range(self.v)]
        stack = []

        for u in range(self.v):
            if not visited[u]:
                stack = self.topologicalSortHelper(visited, u, stack)

        print("Topological Sorting:",end=" ")
        while stack:
            print(stack.pop(),end=" ")
        print()
            
if __name__ == '__main__':
    v = int(input("No.of vertices: "))
    e = int(input("No.of edges: "))
    
    g = Graph(v,e)
    g.topologicalSort()